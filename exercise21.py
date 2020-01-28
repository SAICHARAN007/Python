#functions with returning
def add(nv, v):
    print(f"the items are added {nv} and {v}")
    return nv+v
def sub(nv, v):
    print(f"the items canceled {nv} and {v}")
    return nv-v
def div(nv, v):
    print(f"the items given by complementry by range of {nv} and {v}")
    return nv*v
def mul(nv, v):
    print(f"the items purcheses given rewards of {nv} and {v}")
    return nv/v

#now get clarify the order
given_order=add(10, 12)
unselected_order=sub(22, 18)
complementry=div(2,2)
rewards=mul(10,5)

print(f"the cross check for total order given order {given_order} , removed items {unselected_order} and for complentry {complementry} items with gained {rewards} rewards")

print("here is the clear description of the all items and rewards")
descript = add(given_order, sub(unselected_order, mul(complementry, div(rewards, 6))))
#print(descript)

 

 