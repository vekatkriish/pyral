import sys

from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally('rally1.rallydev.com', 'venkat.kristipati@gmail.com', 'KRIIsh123@%', workspace = 'Workspace 1', project='Sample Project', server_ping=True)
#rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('rally.simple-use.log')

workspaces = rally.getWorkspaces()
for wksp in workspaces:
    print("%s %s" % (wksp.oid, wksp.Name))
    projects = rally.getProjects(workspace=wksp.Name)
    for proj in projects:
        print("    %12.12s  %s" % (proj.oid, proj.Name))

response = rally.get('Release', fetch="Project,Name,ReleaseStartDate,ReleaseDate",
                     order="ReleaseDate")

for release in response:
    rlsStart = rls.ReleaseStartDate.split('T')[0]  # just need the date part
    rlsDate  = rls.ReleaseDate.split('T')[0]       # ditto
    print("%-6.6s  %-16.16s   %s  -->  %s" % \
          (rls.Project.Name, rls.Name, rlsStart, rlsDate))
