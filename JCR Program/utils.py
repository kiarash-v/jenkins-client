
def update_built_file(BuiltFilePath, action, JobName, LocalCreationDate=None, ServerCreationDate=None, ReconfigurationDate=None):
    '''
    Update the local built database file
    :param BuiltFilePath: built file location
    :param action: actions that can be performed are : 'update-server-create-date' , 'update-reconfig-date','update-local-create-date' , 'delete'
    :param LocalCreationDate: date of creation of local config.xml file
    :param ServerCreationDate: date of creation of server job
    :param ReconfigurationDate: date of reconfiguration of server job
    '''

    fh = open(BuiltFilePath)
    BuiltFileLines = []
    FirstLocalCreation=True   # This is for when we are creating config.xml for first time. we want to distinguish between first creatiion and reconfiguration
    for line in fh:
        line = line.strip()
        if line.startswith("#"): pass
        elif JobName == (line.split("@")[-1]):
            if action =='delete':
                # By passing we automatically delete this entry from this database
                pass
            elif action == 'update-server-create-date':
                BuiltFileLines.append("{0}@{1}@{2}@{3}@{4}".format("D", line.split("@")[1], ServerCreationDate, line.split("@")[3], JobName))

            elif action == 'update-reconfigure-date':
                BuiltFileLines.append("{0}@{1}@{2}@{3}@{4}".format("D", line.split("@")[1], line.split('@')[2], ReconfigurationDate, JobName))

            elif action == 'update-deploy-status-ND':
                BuiltFileLines.append("{0}@{1}@{2}@{3}@{4}".format("ND", line.split("@")[1], line.split("@")[2], line.split("@")[3], JobName))

            elif action == 'update-local-create-date':
                BuiltFileLines.append("{0}@{1}@{2}@{3}@{4}".format("ND", LocalCreationDate, 'None', 'None', JobName))

                # If the built file contains an entry for this job and you create a similar config.xml file for that job
                # FirstLocalCreation should be False not True
                FirstLocalCreation=False
        else:
            BuiltFileLines.append(line)

    fh.close()

    if FirstLocalCreation and action=='update-local-create-date':
        BuiltFileLines.append('{0}@{1}@{2}@{3}@{4}'.format('ND', LocalCreationDate, 'None', 'None', JobName))
    fh = open(BuiltFilePath, 'w')
    for line in BuiltFileLines:
        fh.write(line + "\n")
    fh.close()


