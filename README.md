## Report

### Varying number_of_known_people

All of the accuracy scores obtained after changing the value of the variable `number_of_known_people` are equal to 1. Since the `rejection_threshold` has been left at 1.00 and all of the smallest distances between the `test` feature vectors and the database vectors are smaller than 1, even the folder of unknown people ends up associated with one of the people in the database. Therefore, the confusion matrices generated are a n by n (where n is in [1, 10]) identity matrices, showing that there haven't been any unknown people detected at all, and every person in the `training` folder has been associated with another person with an index smaller than `number_of_known_people`.
