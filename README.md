# Hamster to Harvest

A utility script to migrate Hamster time tracking entries to Harvest.

## Installation

### Clone the migration script

    $ git clone git@github.com:olange/hamster-to-harvest.git

### Setup virtual environment

This script uses a [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to keep your Python system installation clean.

If you're not using [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) yet, install it first:

    $ pip install virtualenv

Go to the migration script home folder, create a fresh virtual environment and activate it (below it is named `venv`, but you can name the environment as you like):

    $ cd hamster-to-harvest
    $ virtualenv venv
    $ source venv/bin/activate

### Download dependencies

Finally, retrieve and install the project dependencies:

    $ pip install -r requirements.txt

They will go to the virtual environnement you just previously. From here on you can run the migration script.

## Execution

### Running the script

    $ cd hamster-to-harvest
    $ source venv/bin/activate
    $ python hamster-migrate.py --help

### Cleanup

By the end of your work session, remember to deactivate the virtual environment:

    $ deactivate

## Rationale

TODO

## References

* [hamster-sqlite](https://pypi.python.org/pypi/hamster-sqlite/0.3) API documentation: have a look at the source of [storage.py](https://github.com/projecthamster/hamster/blob/master/src/hamster/storage/storage.py); the package actually wraps `db.py` and `storage.py` from the [Hamster sources](https://github.com/projecthamster/hamster/tree/master/src/hamster/storage) and `storage.py` describes the interface
* [Harvest Time Tracking API](https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md)

## So long

I'll be missing Hamster.

````
        #this is most essential
        if any([b in activity for b in ("bbq", "barbeque", "barbecue")]) and "omg" in activity:
            self.ponies = True
            self.description = "[ponies = 1], [rainbows = 0]"
````

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
