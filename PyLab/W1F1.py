##/////////////////////// PROBLEM STATEMENT //////////////////////////////
## Write a program that that reads two files (filename are input)       //
## containing boys names and girls names and a count for each name.     //
## The format of the files is: name count. Find the most popular        //
## name which is common to boys and girls.                              //
##                                                                      //
##////////////////////////////////////////////////////////////////////////
def dic_from_file(filename):
    dic = dict()
    try:
        file = open(filename)
    except:
        print ("cannot open file: ", filename)
    data = file.read()
    lines = data.splitlines()
    for line in lines:
        myList = line.split(" ")
        name = myList[0]
        count = int(myList[1])
        dic[name] = count
    return dic
#end dic_from_file

filename1 = input()
filename2 = input()
dic1 = dic_from_file(filename1)
dic2 = dic_from_file(filename2)
# refer to https://www.tutorialspoint.com/python/python_dictionary.htm
myList1 = dic1.keys()
myList2 = dic2.keys()
name_set = set(dic1.keys()).intersection(set(dic2.keys()))
common_name_dic = dict()
#myList = []
for name in name_set:
    common_name_dic[name] = dic1[name] + dic2[name]
#Sort the dictionary by value
lst	= list()
for	key, val in	common_name_dic.items():
	lst.append((val, key))
#print (lst)
lst.sort(reverse = True)
(val, key) = lst[0]
print (" Most popular is %s occurring %d times" % (key, val))
#print (common_name_dic)
