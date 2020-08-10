# PSL-Hackathon2020 -- Simple Recommender System

## Problem & Dataset

In this work, we attempt to predict the rating of users based on user-user similarity and item-item similarity for a synthetic dataset. The two original txt files are: 

`rating_obs.txt`: it contains all the observed ratings;
`rating_target.txt`: it contains all the unobserved ratings.




## Model description
1. simple-recommender is the full PSL model which contain item-item similarity rule, user-user similarity rule, and rating similarity rules.
Specifically the rules are:
```
// User similarity

1.0: similarUser(U1, U2) & rating(U1, I1) ->  rating(U2, I1) ^2

// Item similarity 

1.0: similarItem(I1, I2)  & rating(U1, I1) ->  rating(U1, I2) ^2

// Prior
1.0: rating(U,I) = AvgUserRating(U)

```



## How to generate different predicates
To generate different txt files for different predictes, go to the script folder and run `datagen.py` file. It will automatically generate the following files in the `../data/simple-recommender/0/eval` folder:
* items.txt
* users.txt
* rating_new_obs.txt
* rating_new_uno.txt
* SimilarItem.txt
* SimilarUser.txt
* AvgUserRating.txt



## How to run the inference
go to the cli folder and do `./run.sh`, it will automatically generate the rating results in a folder named `infered-predicate`. It will also automatically preform weight learning and generate evaluation results including Accuracy, F1, Positive Class Precision, Positive Class Recall, Negative Class Precision, Negative Class Recall.



