=============
Reference API
=============

.. toctree::
   :maxdepth: 2

   asyncio.rst

.. toctree::
   :maxdepth: 2

   queue.rst

.. toctree::
   :maxdepth: 2

   pool.rst

.. toctree::
   :maxdepth: 2

   base.rst

.. _exceptions:

Exceptions
==========

The exceptions are converted from libchirp error-codes, the attribute `ecode`
contains the original libchirp error-code.

* :py:class:`ValueError`: Bad values, for example: bad config values

* :py:class:`RuntimeError`: Unexpected runtime problems, for example: failed initialization
  of resources, protocol or TLS errors

* :py:class:`OSError`: Address in use

* :py:class:`ConnectionError`: Remote connection denied or closed

* :py:class:`TimeoutError`: Network timeouts

* :py:class:`MemoryError`: libchirp tries to be robust in low-memory situations. Usually
  this means the operation has not completed due to low-memory

* :py:class:`Exception`: libchirp has returned a error that is not mapped in python-chirp.
  You should file an issue if that happens.
