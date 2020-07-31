class DataGen() :
    def users(self, obsFname, unobsFname) :
        obsFile = open(obsFname, "r")
        unobsFile = open(unobsFname, "r")
        userDict = set()
        itemsDict = set()
        usersFile = open("users.txt","w+")
        itemsFile = open("items.txt", "w+")

        f1 = obsFile.readlines()
        for i in f1 :
            row = i.split()
            if row[0] not in userDict:
                userDict.add(row[0])
            if row[1] not in itemsDict:
                itemsDict.add(row[1])

        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            if row[0] not in userDict:
                userDict.add(row[0])
            if row[1] not in itemsDict:
                itemsDict.add(row[1])

        for i in userDict:
            usersFile.write("%s\r\n" %(i))

        for i in itemsDict:
            itemsFile.write("%s\r\n" %(i))

dataObject = DataGen()
dataObject.users("rating_obs.txt", "rating_uno.txt")
