*********
tinynetrc
*********

.. image:: https://badgen.net/pypi/v/tinynetrc
  :alt: pypi badge
  :target: https://pypi.org/project/tinynetrc/

.. image:: https://badgen.net/travis/sloria/tinynetrc/master
  :alt: travis-ci status
  :target: https://travis-ci.org/sloria/tinynetrc

Read and write .netrc files in Python.


``tinynetrc`` uses the `netrc <https://docs.python.org/3/library/netrc.html>`_
module from the standard library under the hood and adds a few
improvements:

* Adds write functionality.
* Fixes a std lib `bug <https://bugs.python.org/issue30806>`_ with
  formatting a .netrc file.*
* Parses .netrc into dictionary values rather than tuples.

\*This bug is fixed in newer versions of Python.

Get it now
==========
::

    pip install tinynetrc


``tinynetrc`` supports Python >= 2.7 or >= 3.5.

Usage
=====

.. code-block:: python

    from tinynetrc import Netrc

    netrc = Netrc()  # parse ~/.netrc
    # Get credentials
    netrc['api.heroku.com']['login']
    netrc['api.heroku.com']['password']

    # Modify an existing entry
    netrc['api.heroku.com']['password'] = 'newpassword'
    netrc.save()  # writes to ~/.netrc

    # Add a new entry
    netrc['surge.surge.sh'] = {
        'login': 'sloria1@gmail.com',
        'password': 'secret'
    }
    netrc.save()

    # Removing an new entry
    del netrc['surge.surge.sh']
    netrc.save()


You can also use ``Netrc`` as a context manager, which will automatically save
``~/.netrc``.

.. code-block:: python

    from tinynetrc import Netrc
    with Netrc() as netrc:
        netrc['api.heroku.com']['password'] = 'newpassword'
        assert netrc.is_dirty is True
    # saved!

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/tinynetrc/blob/master/LICENSE>`_ file for more details.
