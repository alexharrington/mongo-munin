
name = "locked"

def doData():
    lockTime = 0
    for k,v in getServerStatus()["locks"].items():
        if 'timeAcquiringMicros' in v:
            for n in v['timeAcquiringMicros']:
                lockTime += v['timeAcquiringMicros'][n]
    
    print(name + ".value " + str( 100 * (lockTime/getServerStatus()["globalLock"]["totalTime"]) ))

def doConfig():

    print("graph_title MongoDB global write lock percentage")
    print("graph_args --base 1000 -l 0 ")
    print("graph_vlabel percentage")
    print("graph_category MongoDB")

    print(name + ".label " + name)





