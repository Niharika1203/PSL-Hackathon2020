import os
import pandas as pd
from scipy import spatial
import collections
import os


class DataGen() :

    # generate user.txt and item.txt
    def generateUsersItems(self, data_dir):

        obsFnamePath = data_dir + "/rating_obs.txt"
        unobsFnamePath = data_dir + "/rating_uno.txt"

        obsFile = open(obsFnamePath, "r")
        unobsFile = open(unobsFnamePath, "r")
        userdict = collections.defaultdict(list)
        itemsSet = set()


        usersFile = open(data_dir + "/users.txt","w+")
        itemsFile = open(data_dir + "/items.txt", "w+")
        averageFile = open(data_dir + "/AvgUserRating.txt", "w+" )

        f_obs = obsFile.readlines()
        for i in f_obs:
            row = i.split()
            userdict[row[0]].append( (float(row[2])+10)/ 20 )
            itemsSet.add(row[1])

        f_uno = unobsFile.readlines()
        for i in f_uno:
            row = i.split()
            userdict[row[0]].append( (float(row[2])+10)/ 20 )
            itemsSet.add(row[1])
        # generate users.txt
        for i in userdict.keys() :
            usersFile.write("%s\r\n" %(i))
            averageFile.write("%s\t%f\n" %(i, (sum(userdict[i])/len(userdict[i])) ) )
        # generate item.txt
        for i in itemsSet:
            itemsFile.write("%s\r\n" %(i))


    def generateNewRating(self, data_dir) :

        obsFnamePath = data_dir + "/rating_obs.txt"
        unobsFnamePath = data_dir + "/rating_uno.txt"

        obsFile = open(obsFnamePath, "r")
        unobsFile = open(unobsFnamePath, "r")


        ratingObsFile = open(data_dir + "/rating_new_obs.txt","w+")
        ratingUnoFile = open(data_dir + "/rating_new_uno.txt", "w+")

        f1 = obsFile.readlines()
        for i in f1:
            row = i.split()
            val = (float(row[2])+10)/ 20
            row[2] = str(val)
            row_add =  '\t'.join(row)
            ratingObsFile.write("%s\r\n" %(row_add))

        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            val = (float(row[2])+10)/ 20
            row[2] = str(val)
            row_add =  '\t'.join(row)
            ratingUnoFile.write("%s\r\n" %(row_add))

        # generate user_item matrix for rating matrix
    def generateRatingMatrix(self, data_dir):

        obsFnamePath = data_dir + "/rating_obs.txt"

        # get the rating dataframe
        Rating = pd.read_csv(obsFnamePath, sep='\t')
        Rating.columns = ["userID", "itemID", "rating"]
        # generate the rating matrix
        userItemMatrix_df = Rating.pivot_table(index='itemID',columns='userID',values='rating').fillna(0)
        #print(userItemMatrix_df)

        # generate the rating matrix:
        # each row represents an item
        # each col represents a user
        userItemMatrix = userItemMatrix_df.to_numpy()

        numItem = len(userItemMatrix)
        numUser = len(userItemMatrix[0])


        SimilarUserFile = open(data_dir + "/SimilarUser.txt","w+")
        SimilarItemFile = open(data_dir + "/SimilarItem.txt", "w+")

        # compute item-item similarity
        for i in range(numItem):
            for j in range(numItem):
                cosine_similarity = 1 - spatial.distance.cosine(userItemMatrix[i], userItemMatrix[j])
                if cosine_similarity > 0.15 :
                    #cosine_similarity = 0
                    SimilarItemFile.write("%s\t%s\t%f\n" %(i+1,j+1, cosine_similarity))

        # compute user-user similarity
        for i in range(numUser):
            for j in range(numUser):
                cosine_similarity = 1 - spatial.distance.cosine(userItemMatrix[:,i], userItemMatrix[:,j])
                if cosine_similarity > 0.1 :
                    #cosine_similarity = 0
                    SimilarUserFile.write("%s\t%s\t%f\n" %(i+1001,j+1001,cosine_similarity))

    def generateTargetRating(self, data_dir) :

        unobsFnamePath = data_dir + "/rating_uno.txt"

        unobsFile = open(unobsFnamePath, "r")

        ratingTargetFile = open(data_dir + "/rating_target.txt", "w+")


        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            ratingTargetFile.write("%s\t%s\n" %(row[0], row[1]) )



onlyfiles = next(os.walk("../data/hackathon/"))[1] #dir is your directory path as string
#print (len(onlyfiles))


for i in range(len(onlyfiles)):
    dataObject = DataGen()
    data_dir = "../data/hackathon/" + str(i)

    dataObject.generateUsersItems(data_dir)
    dataObject.generateNewRating(data_dir)
    dataObject.generateRatingMatrix(data_dir)
    dataObject.generateTargetRating(data_dir)

