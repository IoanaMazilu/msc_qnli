# defining the ages of the individuals in the premise
age_trevor_premise = 23
age_darcy_premise = 18
age_harriett_premise = 94
age_dave_premise = 74

# defining the ages of the individuals in the hypothesis
age_1_hypothesis = 94
age_2_hypothesis = 74
age_3_hypothesis = 45
age_4_hypothesis = 18

# checking if the ages mentioned in the hypothesis contradict the ages mentioned in the premise
if (age_1_hypothesis not in [age_trevor_premise, age_darcy_premise, age_harriett_premise, age_dave_premise] or 
    age_2_hypothesis not in [age_trevor_premise, age_darcy_premise, age_harriett_premise, age_dave_premise] or 
    age_3_hypothesis not in [age_trevor_premise, age_darcy_premise, age_harriett_premise, age_dave_premise] or 
    age_4_hypothesis not in [age_trevor_premise, age_darcy_premise, age_harriett_premise, age_dave_premise]):
    label = "contradiction"
else:
    label = "neutral"

print(label)
