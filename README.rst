=================
Storm DRPC Client
=================

Storm DPRC Client provides a python clone of the
`backtype.storm.utils.DRPCClient` class shipped along with the
standard storm stream processing package by nathanmarz_ found
here_. You may find it helpful for establishing connections to
and executing remote procedure calls on a running storm DRPC
server.

Typical usage::

    from storm.drpc import DRPCClient

    c = DRPCClient("my.drpc.host", 3772)
    c.execute("wordcounts", "jabberwocky")

Storm DRPC Client inherits the Eclipse Public License from
the original storm project.

Contributors
============

| Thrift generated classes by nathanmarz_.
| Python DRPCClient clone class by strongh_.
| Repackaging for PyPI by mahall_.

.. _nathanmarz: https://github.com/nathanmarz
.. _strongh: https://github.com/strongh
.. _mahall: https://github.com/mahall
.. _here: https://github.com/nathanmarz/storm
