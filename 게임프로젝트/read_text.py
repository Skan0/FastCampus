f=open("voca.txt","r", encoding ="UTF-8")
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
data_list = data_list[:-1]
data_list[-1]=data_list[-1].replace(u"\xa0",u" ").split(" ")
