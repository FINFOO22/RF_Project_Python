def csv_to_dict(filename, simplify_names=True):
    import csv
    with open(f'{filename}', mode='r') as infile_:
        reader = csv.reader(infile_)
        colNames = {} # dictionary that has the index of the column name 
        i = 0
        mydict = {}
        index = 0 # this is to then NAVIGATE THE DICT
        for rows in reader:
            #print(rows)
            #exit()
            #print(rows)
            index = 0
            if i == 0:
                for n in rows:
                    #print(n)
                    if simplify_names:
                        n = ''.join(e for e in n if e.isalnum())
                    mydict[n] = []
                    colNames[i] = n # index corresponds to col name
                    i += 1
                    #print(mydict)
            else:
                pass
                for n in rows:
                    try:
                        mydict[colNames[index]] += [float(n)]
                        #print(index)

                        index += 1
                    except:
                        #print(index)
                        #print(n)
                        #print(len(list(colNames.keys())))
                        #print(colNames)
                        #print(colNames[index])
                        #print(mydict[colNames[index]])

                        #exit()
                        try:
                            mydict[colNames[index]] += [n]
                        except:
                            continue

                        index += 1

        return mydict            
        # this mydict has ALL the 

