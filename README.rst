*********
tinynetrc
*********

.. image:: https://travis-ci.org/sloria/tinynetrc.svg?branch=master
    :target: https://travis-ci.org/sloria/tinynetrc
    :alt: Travis-CI

Read and write .netrc files in Python.


``tinynetrc`` uses the `netrc <https://docs.python.org/3/library/netrc.html>`_
module from the standard library under the hood and adds a few
improvements:

* Adds write functionality.
* Fixes a std lib `bug <https://bugs.python.org/issue30806>`_ with
  formatting a .netrc file.*
* Parses .netrc into dictionary values rather than tuples.

\*This bug is fixed in Python 3.7 but still exists in older versions.

Usage
=====

.. code-block:: python

    from tinynetrc import Netrc

    netrc = Netrc()  # parse ~/.netrc
    netrc.machines['api.heroku.com']['password']  # get auth token

    # Modify an existing entry
    netrc.machines['api.heroku.com']['password'] = 'newpassword'
    netrc.save()  # writes to ~/.netrc

    # Add a new entry
    netrc.machines['surge.surge.sh'] = {
        'login': 'sloria1@gmail.com',
        'password': 'secret'
    }
    netrc.save()

    # Removing an new entry
    del netrc.machines['surge.surge.sh']
    netrc.save()

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/tinynetrc/blob/master/LICENSE>`_ file for more details.
