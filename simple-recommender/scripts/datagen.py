import os
class DataGen() :

    def users(self, obsFname, unobsFname) :
        obsFile = open(obsFname, "r")
        unobsFile = open(unobsFname, "r")
        userset = set()
        itemset = set()
        usersFile = open("users.txt","w+")
        itemsFile = open("items.txt", "w+")

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
print(cur_path)
os.chdir('../')
new_path = os.getcwd() #os.path.relpath('../data/simple-recommender/0/eval/', cur_path)
print(new_path)
dataObject.users(new_path+"/data/simple-recommender/0/eval/rating_obs.txt", new_path+"/data/simple-recommender/0/eval/rating_uno.txt")
