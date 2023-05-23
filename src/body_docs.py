
name = "documents"

def getDatabasesStats():
    c = getClient()

    dbs = {}
    for k in c.list_database_names():
        if k != "admin" and k != "local" and k != "":
            db = c[k]
            dbs[k] = {}
            for coll in db.list_collection_names():
                if '.' not in coll:
                    dbs[k][coll] = db[coll].estimated_document_count()

    return dbs

def doData():
    ss = getDatabasesStats()
    for k,v in ss.items():
        for a,b in v.items():
            print((str(k)+str(a) + ".value " + str(b)))


def doConfig():

    print("graph_title MongoDB documents count")
    print("graph_args --base 1000 -l 0 --vertical-label Docs")
    print("graph_category MongoDB")

    ss = getDatabasesStats()
    for k,v in ss.items():
        for a,b in v.items():
            print(str(k)+str(a) + ".label " + str(k) + " " + str(a))
            print(str(k)+str(a) + ".draw LINE1")

