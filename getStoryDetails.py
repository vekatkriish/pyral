import sys

from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally('rally1.rallydev.com', 'venkat.kristipati@gmail.com', 'KRIIsh123@%', workspace = 'Workspace 1', project='Sample Project', server_ping=True)
#rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('rally.simple-use.log')

response = rally.get('Defect', fetch=True, query='FormattedID = DE2')
story1 = response.next()
print(story1.Notes)