import sys

from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally('rally1.rallydev.com', 'venkat.kristipati@gmail.com', 'KRIIsh123@%', workspace = 'Workspace 1', project='Sample Project', server_ping=True)
#rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('rally.simple-use.log')

args = sys.argv
#print(args)
#defectID, notes = args[:2]
# target_date must be in ISO-8601 format "YYYY-MM-DDThh:mm:ssZ"
proj = rally.getProject()

defectID = sys.argv[1]
notes = sys.argv[2]

defect_data = { "FormattedID" : defectID,
                "Notes"       : notes
               }
try:
    defect = rally.update('Defect', defect_data)
except Exception as details:
    sys.stderr.write('ERROR: %s \n' % details)
    sys.exit(1)

print("Defect %s updated" % defect.FormattedID)