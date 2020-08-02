import os
class DataGen() :

    def users(self, parDir) :
        obsFile = open(parDir+"rating_obs.txt", "r")
        unobsFile = open(parDir+"rating_uno.txt", "r")
        userset = set()
        itemset = set()
        usersFile = open(parDir+"users.txt","w+")
        itemsFile = open(parDir+"items.txt", "w+")

        f1 = obsFile.readlines()
        for i in f1 :
            row = i.split()
            userset.add(row[0])
            itemset.add(row[1])

        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            userset.add(row[0])
            itemset.add(row[1])

        for i in userset:
            usersFile.write("%s\r\n" %(i))

        for i in itemset:
            itemsFile.write("%s\r\n" %(i))

dataObject = DataGen()
cur_path = os.getcwd()
# print(cur_path)
os.chdir('../')
new_path = os.getcwd()
new_path += "/data/simple-recommender/0/eval/"
# print(new_path)
dataObject.users(new_path)
