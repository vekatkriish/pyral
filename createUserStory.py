import sys

from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally('rally1.rallydev.com', 'venkat.kristipati@gmail.com', 'KRIIsh123@%', workspace = 'Workspace 1', project='Sample Project', server_ping=True)
#rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('rally.simple-use.log')

proj = rally.getProject()

# get the first (and hopefully only) user whose DisplayName is 'Sally Submitter'
user = rally.getUserInfo(name='VENKAT KRIISH').pop(0)

userStory_data = { "Name": "Hello2",
				   "Notes": "Hello Notes",
                   "Description" : "This is a sample user story for jenkins automation" }
try:
    ustory = rally.create('UserStory', userStory_data)
except Exception as details:
    sys.stderr.write('ERROR: %s \n' % details)
    sys.exit(1)
print("ustory created, ObjectID: %s  FormattedID: %s" % (ustory.oid, ustory.FormattedID))
