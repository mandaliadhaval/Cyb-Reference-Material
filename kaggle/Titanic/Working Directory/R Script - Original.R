#Setup Working Directory
setwd("D:/Machine Learning/Kaggle/Titanic/Working Directory")
#Import Train.csv dataset
library(readr)
train <- read_csv("D:/Machine Learning/Kaggle/Titanic/Dataset/train.csv")
View(train)

## Data import completed. 891 observations with 12 variables in the dataframe
## Add new column Survived1 with scenario of all died
train["Survived1"]<-0
## Set survived1=1 where Sex is female
train$Survived1[train$Sex=='female']<-1
summary(train$Age)
train$Child <- 0
train$Child[train$Age < 18] <- 1

test$Survived <- 0 #All perished
test$Survived[test$Sex == 'female'] <- 1 #Only female Survived
test$Survived[test$Sex == 'female' & test$Pclass == 3 & test$Fare >= 20] <- 0 #Class 3 Female who paid more than $20 perished
# Score 0.779
# Moving to algorithms. Installed Library rpart - Recursive Partitioning and Regression Trees
