from evaluate_all_model import EvaluateAllModels
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
import pandas as pd
import numpy as np

model_type = "xlm"

#EvaluateAllModels.get_predictions(model_type)


file = open('predictions_output_'+model_type+'.csv', encoding="utf8")

# Load the data
data = pd.read_csv(file)

# Split the data into features (X), target (y), and predictions (y_pred)
X = data.drop(['target', 'prediction'], axis=1)
y = data['target']
y_pred = data['prediction']

# Convert the target and predictions to numpy arrays
y = np.array(y)
y = np.array([str(y_i) for y_i in y])
y_pred = np.array(y_pred)


labels = np.unique(y)
print("Target labels:", labels)

# Set the pos_label based on the unique labels in the target column
pos_label = labels[1]

# Calculate the precision
prec = precision_score(y, y_pred, pos_label=pos_label,average='macro')

# Calculate the recall
recall = recall_score(y, y_pred, pos_label=pos_label,average='macro')

# Calculate the f1
f1 = f1_score(y, y_pred, pos_label=pos_label,average='macro')

# Calculate the acc
acc = f1_score(y, y_pred, pos_label=pos_label,average='macro')

# Print the results
print("F1 score: %0.2f" % f1)
print("Accuracy: %0.2f" % acc)
print("Precision: %0.2f" % prec)
print("Recall: %0.2f" % recall)


