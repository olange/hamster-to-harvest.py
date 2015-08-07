import harvest.api
import config

cfg = config.read( 'hamster-migrate.cfg')

harvest_url = cfg.get( 'Harvest', 'url')
harvest_email = cfg.get( 'Harvest', 'email')
harvest_pwd = cfg.get( 'Harvest', 'password')
h = harvest.api.Harvest( harvest_url, harvest_email, harvest_pwd)

for project in h.projects():
  print u"Project %s (%s)\n Client %s" % (project.name, project.id, project.client.name)
  for assignment in project.task_assignments:
    print u'\t%s' % assignment
