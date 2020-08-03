import os
import pandas as pd
from scipy import spatial

class DataGen() :

    # generate user.txt and item.txt
    def generateUsersItems(self, obsFnamePath, unobsFnamePath) :
        obsFile = open(obsFnamePath, "r")
        unobsFile = open(unobsFnamePath, "r")
        userSet = set()
        itemsSet = set()

        cwd = os.getcwd()
        parent_cwd = os.path.dirname(cwd)
        data_dir = parent_cwd + "/data/simple-recommender/0/eval"
        #print(data_dir)

        usersFile = open(data_dir + "/users.txt","w+")
        itemsFile = open(data_dir + "/items.txt", "w+")

        f_obs = obsFile.readlines()
        for i in f_obs:
            row = i.split()
            userSet.add(row[0])
            itemsSet.add(row[1])

        f_uno = unobsFile.readlines()
        for i in f_uno:
            row = i.split()
            userSet.add(row[0])
            itemsSet.add(row[1])
        # generate users.txt
        for i in userSet:
            usersFile.write("%s\r\n" %(i))
        # generate item.txt
        for i in itemsSet:
            itemsFile.write("%s\r\n" %(i))


    def generateNewRating(self, obsFnamePath, unobsFnamePath) :
        obsFile = open(obsFnamePath, "r")
        unobsFile = open(unobsFnamePath, "r")

        cwd = os.getcwd()
        parent_cwd = os.path.dirname(cwd)
        data_dir = parent_cwd + "/data/simple-recommender/0/eval/"
        #print(data_dir)


        ratingObsFile = open(data_dir + "rating_new_obs.txt","w+")
        ratingUnoFile = open(data_dir + "rating_new_uno.txt", "w+")

        f1 = obsFile.readlines()
        for i in f1:
            row = i.split()
            val = (float(row[2])+10)/ 20
            if val >= 0.75 :
                row[2] = str(val)
                row_add =  '\t'.join(row)
                ratingObsFile.write("%s\r\n" %(row_add))

        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            val = (float(row[2])+10)/ 20
            if val >= 0.75 :
                row[2] = str(val)
                row_add =  '\t'.join(row)
                ratingUnoFile.write("%s\r\n" %(row_add))

        # generate user_item matrix for rating matrix
    def generateRatingMatrix(self, obsFnamePath):
        cwd = os.getcwd()
        #print(cwd)
        parent_cwd = os.path.dirname(cwd)
        data_dir = parent_cwd + "/data/simple-recommender/0/eval"

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
                if cosine_similarity < 0:
                    cosine_similarity = 0
                SimilarItemFile.write("%s\t%s\t%f\n" %(i+1,j+1,cosine_similarity))

        # compute user-user similarity
        for i in range(numUser):
            for j in range(numUser):
                cosine_similarity = 1 - spatial.distance.cosine(userItemMatrix[:,i], userItemMatrix[:,j])
                if cosine_similarity < 0:
                    cosine_similarity = 0
                SimilarUserFile.write("%s\t%s\t%f\n" %(i+1001,j+1001,cosine_similarity))

    def generateTargetRating(self, unobsFnamePath) :
        unobsFile = open(unobsFnamePath, "r")

        cwd = os.getcwd()
        parent_cwd = os.path.dirname(cwd)
        data_dir = parent_cwd + "/data/simple-recommender/0/eval/"
        #print(data_dir)

        #ratingObsFile = open(data_dir + "rating_new_obs.txt","w+")
        ratingTargetFile = open(data_dir + "rating_target.txt", "w+")


        f2 = unobsFile.readlines()
        for i in f2 :
            row = i.split()
            ratingTargetFile.write("%s\t%s\n" %(row[0], row[1]))




dataObject = DataGen()

cwd = os.getcwd()
parent_cwd = os.path.dirname(cwd)
filename_obs = parent_cwd + '/data/simple-recommender/0/eval/rating_obs.txt'
filename_uno = parent_cwd +'/data/simple-recommender/0/eval/rating_uno.txt'

dataObject.generateUsersItems(filename_obs, filename_uno)
dataObject.generateNewRating(filename_obs, filename_uno)
dataObject.generateRatingMatrix(filename_obs)
dataObject.generateTargetRating(filename_uno)
