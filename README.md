# Hamster to Harvest

A utility script written in Python to migrate [Hamster](http://projecthamster.wordpress.com/about/) time tracking entries to the [Harvest](https://www.getharvest.com) time tracking web service.

## Status

Currently a work-in-progress, in pre-alpha stage.

## Installation

### Download the migration script

    $ git clone git@github.com:olange/hamster-to-harvest.git

### Setup a Python virtual environment

If you're not using [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) yet, I'd recommend you to install it first; it will keep your Python system installation clean:

    $ pip install virtualenv

Then go to the migration script home folder, create a fresh virtual environment and activate it (below it is named `venv`, but you can name the environment as you like):

    $ cd hamster-to-harvest
    $ virtualenv venv
    $ source venv/bin/activate

### Install dependencies

Retrieve and install the project dependencies:

    $ pip install -r requirements.txt

They will go to the virtual environnement you created previously. From here on you can run the migration script.

## Execution

### Setup

    $ cd hamster-to-harvest
    $ source venv/bin/activate

### Configure

First, create a configuration file `hamster-migrate.cfg` from the template:

    $ cp hamster-migrate.cfg.sample hamster-migrate.cfg

and setup your Harvest authentication credentials in `hamster-migrate.cfg`.

Then, place a copy of your Hamster database into the `data/` subfolder. The database should be named `hamster.db`.

Alternatively, you could change the `database-dir` configuration option in the `[Hamster]` section of the configuration to point to your Hamster applet live database; on Ubuntu, you'd define it like this:

    [Hamster]
    database-dir = ~/.local/share/hamster-applet
    ...

### Getting help

    $ python hamster-migrate.py --help

### Cleanup

By the end of your work session, remember to deactivate the virtual environment:

    $ deactivate

## Rationale

Hamster having no bulk edit feature, marking time entries as being invoiced was impractical to me. And the reporting was missing a few features I needed for my invoicing.

Hamster being written in Python, and me liking it, I wrote a Python batch script to switch an `uninvoiced` tag to `invoiced` – and also wrote my own reporting template.

Yet it remained tedious for each and every invoice. I had to fix encoding and formatting in the invoices, despite having written a custom template.

Lacking time to contribute changes to the codebase, one day I switched to the Harvest web service.

Recently, I needed to consolidate all time entries from Harvest, Hamster and another system I was using. As Hamster is currently not maintained (see Toms Bauģis' [announcement of 18.08.2014](https://github.com/projecthamster/hamster/blob/9aa618b023f89684526dfd816ef8aeabdce360bf/README.textile)), it was clear the target of the consolidation was going to be Harvest. Hence the need for this migration script.

## References

* [Harvest API](https://github.com/harvesthq/api)
* API documentation of the [hamster-sqlite](https://pypi.python.org/pypi/hamster-sqlite/0.3) package: have a look at the source of [storage.py](https://github.com/projecthamster/hamster/blob/master/src/hamster/storage/storage.py); the package actually wraps `db.py` and `storage.py` from the [Hamster sources](https://github.com/projecthamster/hamster/tree/master/src/hamster/storage)

## So long

I'll be missing Hamster. The applet had a nicely designed user interface and the authors a unique and distinctive voice, that could be appreciated on the blog or found in the sources.

````
        #this is most essential
        if any([b in activity for b in ("bbq", "barbeque", "barbecue")]) and "omg" in activity:
            self.ponies = True
            self.description = "[ponies = 1], [rainbows = 0]"
````

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
