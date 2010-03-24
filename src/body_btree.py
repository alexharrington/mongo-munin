
def get():
    return getServerStatus()["indexCounters"]["btree"]

def doData():
    for k,v in get().iteritems():
        print( str(k) + ".value " + str(v) )

def doConfig():

    print "graph_title MongoDB memory usage"
    print "graph_args --base 1000"
    print "graph_vlabel mb ${graph_period}"
    print "graph_category MongoDB"

    for k in get():
        print k + ".label " + k
        print k + ".min 0"
        print k + ".type COUNTER"
        print k + ".max 500000"
        print k + ".draw AREA"




