"""Loop tests."""
from concurrent.futures import Future
import gc
from libchirp import Loop
import pytest
import threading


def test_loop_lifecycle(caplog):
    """test_loop_lifecycle."""
    a = Loop()
    a.run()
    assert len(gc.get_referrers(a)) > 1
    assert a.running
    a.stop()
    assert not a.running
    assert len(gc.get_referrers(a)) == 1
    assert caplog.record_tuples == [
        ('libchirp', 10, 'libuv event-loop started'),
        ('libchirp', 10, 'libuv event-loop stopped'),
    ]


def get_thread(fut: Future):
    """get_thread."""
    fut.set_result(threading.current_thread())


def test_call_soon():
    """test_call_soon."""
    loop = Loop()
    try:
        loop.run()
        assert loop.running
        fut = Future()
        loop.call_soon(get_thread, fut)
        fut.result() == loop._thread
    finally:
        loop.stop()
        assert not loop.running


def test_call_soon_reverse():
    """test_call_soon_reverse."""
    loop = Loop()
    try:
        fut = Future()
        loop.call_soon(get_thread, fut)
        assert not loop.running
        loop.run()
        assert loop.running
        fut.result() == loop._thread
    finally:
        loop.stop()
        assert not loop.running


def test_start_stop_orders():
    """test_start_stop_orders."""
    loop = Loop()
    try:
        assert not loop.running
        loop.stop()
        assert not loop.running
        loop.run()
        assert loop.running
        loop.run()
        assert loop.running
        loop.stop()
        assert not loop.running
        with pytest.raises(RuntimeError):
            loop.run()
    finally:
        loop.stop()
        assert not loop.running