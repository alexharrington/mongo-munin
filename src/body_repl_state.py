

def doData():
    primary = getServerStatus()["repl"]["ismaster"]
    secondary = getServerStatus()["repl"]["secondary"]
    
    if primary:
        print("primary.value 1")
        print("secondary.value 0")
    elif secondary:
        print("primary.value 0")
        print("secondary.value 1")
    else:
        print("primary.value 0")
        print("secondary.value 0")

def doConfig():

    print("graph_title MongoDB Replication State")
    print("graph_args --base 1000 -l 0 -u 1")
    print("graph_vlabel State")
    print("graph_category MongoDB")

    for k in ('primary', 'secondary'):
        print(k + ".label " + k)
        print(k + ".min 0")
        print(k + ".type COUNTER")
        print(k + ".max 1")
        print(k + ".draw LINE1")
