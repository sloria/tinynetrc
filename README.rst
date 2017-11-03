*********
tinynetrc
*********


Reading ``~/.netrc``
====================

.. code-block:: python

    from tinynetrc import Netrc

    netrc = Netrc()  # parse ~/.netrc
    netrc.machines['api.heroku.com']['password']  # get auth token

Writing ``~/.netrc``
====================

.. code-block:: python

    from tinynetrc import Netrc

    netrc = Netrc()
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
