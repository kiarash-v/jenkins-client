#
# def columnify(iterable):
#     # First convert everything to its repr
#     strings = [str(x) for x in iterable]
#     # Now pad all the strings to match the widest
#     widest = max(len(x) for x in strings)
#
#     padded = [x.ljust(widest) for x in strings]
#     return padded
#
# def colprint(iterable, width=72):
#     columns = columnify(iterable)
#     colwidth = len(columns[0]) + 2
#     perline = (width - 4) // colwidth
#
#     for i, column in enumerate(columns):
#         if ' ' in column.strip():
#             print("\'{0}\'".format(column.strip()),end=' ')
#         else:
#             print(column,end=' ')
#         if i % perline == perline - 1:
#                 print()
#     print()


def print_column(data):
    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print("".join(word.ljust(col_width) for word in row))


def print_columny(row_data, column_titiles, column_sizes):
    col_width = max(len(word) for row in row_data for word in row) + 2  # padding
    for i in range(len(column_titiles)):
        print(column_titiles[i].ljust(column_sizes[i]), end='')

    print()
    for i in range(len(column_titiles)):
        print(("-" * (len(column_titiles[i]))).ljust(column_sizes[i]), end='')

    print()

    for row in row_data:
        for i in range(len(row)):
            print(row[i].ljust(column_sizes[i]), end='')
        print()




def update_built_file(configpath ,action , jobname , local_creating_date=None , server_creation_date=None , reconfig_date=None):
    '''
    Update the local built database file
    :param configpath: built file location
    :param action: actions that can be performed are : 'update-server-create-date' , 'update-reconfig-date','update-local-create-date' , 'delete'
    :param local_creating_date: date of creation of local config.xml file
    :param server_creation_date: date of creation of server job
    :param reconfig_date: date of reconfiguration of server job
    '''

    fhandle = open(configpath)
    lines = []
    local_create=True   # This is for when we are creating config.xml for first time. we want to distinguish between first creatiion and reconfiguration
    for line in fhandle:
        line = line.strip()
        if line.startswith("#"):
            pass
        elif jobname == (line.split("@")[-1]):
            if action =='delete':
                # By passing we automatically delete this entry from this database
                pass
            elif action == 'update-server-create-date':
                lines.append("{0}@{1}@{2}@{3}@{4}".format("D",line.split("@")[1],server_creation_date , line.split("@")[3] , jobname))

            elif action == 'update-reconfigure-date':
                lines.append("{0}@{1}@{2}@{3}@{4}".format("D", line.split("@")[1] , line.split('@')[2] , reconfig_date , jobname))

            elif action == 'update-deploy-status-ND':
                lines.append("{0}@{1}@{2}@{3}@{4}".format("ND",line.split("@")[1],line.split("@")[2], line.split("@")[3] , jobname))

            elif action == 'update-local-create-date':
                lines.append("{0}@{1}@{2}@{3}@{4}".format("ND", local_creating_date, 'None' , 'None' , jobname))

                # The job entry was preiously in the file and you create a similar config.xml file for that job
                # so local_create is False in this case
                local_create=False
        else:
            lines.append(line)

    fhandle.close()

    if local_create and action=='update-local-create-date':
        lines.append('{0}@{1}@{2}@{3}@{4}'.format('ND',local_creating_date ,'None','None' ,jobname))
    fhandle = open(configpath, 'w')
    fhandle.write("## STAT (D / ND) ## CRL ## CRS ## RCFG ## Job\n")
    for line in lines:
        fhandle.write(line + "\n")
    fhandle.close()


