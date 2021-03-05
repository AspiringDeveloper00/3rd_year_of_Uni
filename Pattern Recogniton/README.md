This is by far the most difficult project until now in university. I learned a lot of things about pattern recogniton and I created a starting point for me to 
comprehend deep learning. Some of the algorithms and classifiers i learned about were the Bayesian classifier, perceptron classification, least mean square algorithm 
for classification and regression, mean square error and finally some feed forward, linear and multilayer neural networks. The assignment is given in greek but it;s simple to 
eexplain. Firstly we had to download some sql file containing football data. After using the EuropeanSoccerDatabaseRetriever.m file we run somw sql queries to get the tables
we have to work with. The first and second algorithms (lms,mse) were used to find which of the 4 given betting companies was the most accurate regarding the outcomes
of football matches. The matches in the database were around 22500. The 10 fold cross validation method was used for the traing and testing procedures. Because we had to deal 
with a 3 class classification problem due to the 3 match outcomes (home win, draw and away team), we had to use either one vs all (which was slow and not clever) or 
(the method we used) one hot vector encoding. This means we vectorized the outcomes like so: 1 0 0 for a home win, 0 1 0 for a draw and 0 0 1 for an away win.
For the third exercise we had a 28 attribute vector for each match (8 numbers rerpresenting the home team attributes, 8 numbers rerpresenting the away team attributes 
and 12 bets-3 for each of the 4 betting companies) from which I trained and tested a multilayer feed forward neural netword for the 3 class classification. 
