#!/usr/bin/python
# -*- coding: utf_8 -*-
# $Id: hamster-update.py 429 2011-11-07 11:36:34Z olange@petit-atelier.ch $

"""Script utilitaire permettant de mettre à jour les tags (étiquettes)
d'un ensemble d'événements de l'application Hamster Applet.
Attention: script sans paramètres, à mettre à jour pour chaque usage."""

import hamster.client
import datetime as dt
import dbus
import sys, getopt

storage = hamster.client.Storage()

# Méthodes utilitaires pour ajouter/enlever un tag
def add_tag( fact, tag):
  t = set( fact['tags']) | set( [ dbus.String( tag)])
  fact[ 'tags'] = dbus.Array( list( t))
  return fact

def remove_tag( fact, tag):
  t = set( fact['tags']) - set( [ dbus.String( tag)])
  fact[ 'tags'] = dbus.Array( list( t))
  return fact

def update_fact( fact):
  new_id = storage.update_fact(
    fact['id'], fact['name'], tags = fact['tags'],
    start_time = fact['start_time'], end_time = fact['end_time'],
    category_name = fact['category'], description = fact['description'],
    temporary = False)
  return new_id

def main():
  # Lecture des arguments
  dryrun = False
  opts, args = getopt.getopt( sys.argv[1:], "hx:", [ "dry-run", "exclude=", "help", "outputdir=", "overwrite"])
  for opt, val in opts:
    if opt == "--dry-run":
      dryrun = True

  # Liste des événements à traiter
  d1 = dt.date( 2011, 01, 01)
  d2 = dt.date( 2011, 10, 31)
  facts = storage.get_facts( d1, d2, "RZO* -PAGLadmin")

  # Mise à jour des événements: suppression du tag 'à facturer'
  count = 0
  for f in facts:
    # f = remove_tag( f, u'à facturer')
    f = add_tag( f, u'facturé')
    print "%5d (%s@%s / %s) %s" % ( f['id'], f['name'], f['category'], ", ".join( f['tags']), f['description'])
    if not( dryrun):
      new_id = update_fact( f)
      print "... updated (new id=%d)\n" % new_id,
    count += 1

  print "{0:d} facts {1}updated.".format( count, dryrun and "would be " or "")

# Amorce exécutable du programme
if __name__ == '__main__':
  main()

# eof
