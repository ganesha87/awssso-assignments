import yaml
from yaml.loader import SafeLoader

newLine = '\n'

with open('teams.yml') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))

    strAssignments = ''
    print('account_assignments = [')
    for fTeam in data:
        if fTeam is None:
            continue
        
        teamName = fTeam['Functional_Team_name']
        for account in fTeam['assignments']['accounts']:
            for permission in account['permissions']:
                strAssignment = '  {'+newLine

                strAssignment = strAssignment + '    account             = "'+account['account_name']+'",'+newLine
                strAssignment = strAssignment + '    permission_set_arn  = "'+permission+'",'+newLine
                strAssignment = strAssignment + '    permission_set_name = "'+permission+'",'+newLine
                strAssignment = strAssignment + '    principal_type = "GROUP",'+newLine
                strAssignment = strAssignment + '    principal_name = "'+ teamName +'"' + newLine

                strAssignment = strAssignment + '  },'+newLine
                strAssignments = strAssignments + strAssignment
        
        #strAssignments = strAssignments + strAssignments[:-2] + ',' + newLine
        #print(strAssignments[:-2])

    print(strAssignments[:-2]+newLine+']')

