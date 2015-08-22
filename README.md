# Hamster to Harvest

A utility script written in Python to migrate [Hamster](http://projecthamster.wordpress.com/about/) time tracking entries to the [Harvest](https://www.getharvest.com) time tracking web service.

## Status

Alpha stage. It is possible to migrate tasks from Hamster to Harvest, but the migration
operations have to be hardcoded within the [commands/migrate.py](commands/migrate.py) script.

Source is not maintained anymore. This project is an early abandoned attempt to migrate Hamster activities directly
from its SQL database into Harvest, thru Harvest's REST API.

Superceded by the [hamster-to-harvest-csv](https://github.com/olange/hamster-to-harvest-csv)
project, which uses another approach: it converts Hamster activities exported as an XML file
to a CSV file, ready to be imported in Harvest thru its _CSV Import_ interface, available
online in the Harvest webapp. The CSV interface has the drawback that it cannot currently
set the _Started at_, _Ended at_ and _Billed?_ fields, which could be defined thru
Harvest's REST API.

For Hamster users, this repo contains a few [goodies](./goodies/) that might prove useful; see below.

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

I needed to consolidate all time entries from Harvest, Hamster and another home grown
system I was using. As Hamster was not maintained anymore (see Toms Bauģis' [announcement
of 18.08.2014](https://github.com/projecthamster/hamster/blob/9aa618b023f89684526dfd816ef8aeabdce360bf/README.textile)),
I decided to consolidate them to Harvest. Hence the need for a migration script.

I switched to Harvest because it was widely available from anywhere, and also because Hamster was missing a few key features: a bulk edit feature to mark time entries as being invoiced (I wrote a small utility script to handle this, see the goodies hereafter); and the reporting was missing a few features.

## References

* [Harvest API](https://github.com/harvesthq/api)
* API documentation of the [hamster-sqlite](https://pypi.python.org/pypi/hamster-sqlite/0.3) package: have a look at the source of [storage.py](https://github.com/projecthamster/hamster/blob/master/src/hamster/storage/storage.py); the package actually wraps `db.py` and `storage.py` from the [Hamster sources](https://github.com/projecthamster/hamster/tree/master/src/hamster/storage)

## So long

I'll be missing Hamster. The applet had a nicely designed user interface. It evolved
in interesting graphical and user interface experiments. And there was an irreverent,
creative and cheerful tone in the project's communications.

````
        #this is most essential
        if any([b in activity for b in ("bbq", "barbeque", "barbecue")]) and "omg" in activity:
            self.ponies = True
            self.description = "[ponies = 1], [rainbows = 0]"
````

## Goodies

[hamster-update.py](goodies/hamster-update.py) is a script that rewrites tags on Hamster facts. The operations are hardcoded, you would need to change them, as well as the query criterias (date range, projects) within the script itself.

[harvest-projects-and-tasks-list.py](goodies/harvest-projects-and-tasks-list.py) is a simple code fragment to retrieve the list of projects and tasks from the Harvest API. You get the same by running `python hamster-migrate.py seed`.

[report_template.html](goodies/report_template.html) is an alternative template to the one delivered with Hamster, that I used to report time and deliver with my invoices.

## Known issues

The following message might be displayed when running the `hamster-migrate.py` script on machines with an OS other than Ubuntu; the Hamster Python library is looking for another library `gio`, available with Ubuntu only. You can safely ignore this message:

````
WARNING:root:Could not import gio - requires pygobject. File monitoring will be disabled
````

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
