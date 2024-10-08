import cv2
import numpy as np

from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy.spatial.distance import cosine
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

import os
from glob import glob

# This method takes as input the face recognition model and the filename of the image and returns
# the feature vector
def extract_features(face_reco_model, filename):
    faceim = cv2.imread(filename)
    faceim = cv2.resize(faceim, (224,224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim)).flatten()
    return feature_vector

# Number of subjects in the training set
number_of_known_people = 10
# Number of images stored for a known person
number_of_training_images_per_person = 10
# Maximum distance for considering a test sample as a face of a known person
rejection_threshold = 0.3
# Dataset path - Folder in which you extracted fr_dataset.zip, you can use relative path
dataset_path = ''

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')

# Create the database of known people
database = []
training_path = os.path.join(dataset_path, 'fr_dataset', 'training')
for i in range(number_of_known_people):
    person_path = os.path.join(training_path, str(i).zfill(2))
    count = 0
    person = []
    for filename in glob(os.path.join(person_path,'*.jpg')):
        if count < number_of_training_images_per_person:
            feature_vector = extract_features(face_reco_model, filename)
            person.append({"id": i, "feature_vector": feature_vector, "filename": filename})
            count += 1
            print("Loading %d - %d"%(i, count))
    database.append(person)

# Print information about the database of known people
for i in range(number_of_known_people):
    for j in range(number_of_training_images_per_person):
        print("%d %s"%(database[i][j]['id'], database[i][j]['filename'])) 

# For each test sample, compute the feature vector and the cosine distance 
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html) 
# with all the known people and: 
# (1) if the minimum distance is less than the rejection threshold, associate the more similar person; 
# (2) otherwise, the face belongs to an unknown person.
# Here (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) 
# and here (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) 
# you find scikit-learn accuracy and confusion matrix documentation
# In groundtruth you must insert for each sample the correct label, while in the predictions the predicted label. 
groundtruth = []
predictions = []
test_path = os.path.join(dataset_path, 'fr_dataset', 'test')
for i in range(11):
    person_path = os.path.join(test_path, str(i).zfill(2))
    for filename in glob(os.path.join(person_path, '*.jpg')):
        test_feature_vector = extract_features(face_reco_model, filename)
        
        min_distance = float('inf')
        predicted_label = 10

        for j in range(number_of_known_people):
            for person in database[j]:
                distance = cosine(test_feature_vector, person['feature_vector'])

                if distance < min_distance:
                    min_distance = distance
                    predicted_label = j
        
        if min_distance > rejection_threshold:
            predicted_label = 10

        groundtruth.append(i)
        predictions.append(predicted_label)

# 1) Try different values between 1 and 10 for number_of_known_people
#   Report accuracies (with a chart if you prefer) and confusion matrices and discuss the results
# 2) Try different values between 1 and 10 number_of_training_images_per_person
#   Report accuracies (with a chart if you prefer) and confusion matrices and discuss the results
# 3) Try different values between 0.1 and 1.0 for the rejection_threshold
#   Report accuracies (with a chart if you prefer) and confusion matrices and discuss the results
print("Accuracy score: %.3f" % (accuracy_score(groundtruth, predictions)))
print("Normalized confusion matrix\n %s" % (confusion_matrix(groundtruth, predictions, normalize='true')))
