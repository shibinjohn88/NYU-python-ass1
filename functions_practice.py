def hello ():
    print ("Hi welcome to Python")

def pack (item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch (list):
    if len(list) == 0:
        print ('My lunchbox is empty')
    else:
        print (f"First I eat {list[0]}")
        if len(list) > 1:
            for i in range(1, len(list)):
                print (f"Next I eat {list[i]}")


hello ()
print (pack ('apple', 'orange', 'grapes'))
eat_lunch (['eggs', 'bread', 'orange'])
eat_lunch ([])
eat_lunch (['eggs'])



