import pandas as pd
import numpy as np

math_scores = pd.read_csv('MathScoreTerm1.csv')
ds_scores = pd.read_csv('DSScoreTerm1.csv')
physics_scores = pd.read_csv('PhysicsScoreTerm1.csv')

math_scores = math_scores.drop(['Name', 'Ethnicity'], axis=1)
ds_scores = ds_scores.drop(['Name', 'Ethnicity'], axis=1)
physics_scores = physics_scores.drop(['Name', 'Ethnicity'], axis=1)

math_scores = math_scores.fillna(0)
ds_scores = ds_scores.fillna(0)
physics_scores = physics_scores.fillna(0)

merged_scores = pd.merge(math_scores, ds_scores, on='StudentID')
merged_scores = pd.merge(merged_scores, physics_scores, on='StudentID')

merged_scores['Sex'] = merged_scores['Sex'].map({'M': 1, 'F': 2})

merged_scores.to_csv('ScoreFinal.csv', index=False)

ethnicity_mapping = {'Asian': 1, 'African American': 2, 'Caucasian': 3, 'Hispanic': 4, 'Other': 5}
merged_scores['Ethnicity'] = merged_scores['Ethnicity'].map(ethnicity_mapping)

merged_scores = merged_scores.replace(0, np.nan)
merged_scores = merged_scores.apply(lambda x: x.fillna(x.mean()), axis=0)

merged_scores.to_csv('ScoreFinal_Enhanced.csv', index=False)
