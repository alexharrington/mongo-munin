

def doData():
    master = getServerStatus()["repl"]["ismaster"]
    secondary = getServerStatus()["repl"]["secondary"]
    
    if master:
        print("isprimary.value 1")
        print("secondary.value 0")
    elif secondary:
        print("isprimary.value 0")
        print("secondary.value 1")
    else:
        print("isprimary.value 0")
        print("secondary.value 0")

def doConfig():

    print("graph_title MongoDB Replication State")
    print("graph_args --base 1000 -l 0 -u 1")
    print("graph_vlabel State")
    print("graph_category MongoDB")

    for k in ('isprimary', 'secondary'):
        print(k + ".label " + k)
        print(k + ".min 0")
        print(k + ".type COUNTER")
        print(k + ".max 1")
        print(k + ".draw LINE1")
