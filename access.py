import frstcode1 as y

y.create("vinitha",10)
y.create("extra",60,3600) 
y.read("vinitha")
y.read("extra")
y.create("vinitha",50)
y.modify("vinitha",55)
y.delete("vinitha")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

