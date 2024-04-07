# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is 5:3.
# Golden Label: contradiction

# Defining the ratio of ages in the premise
arun_age_premise = 4
deepak_age_premise = 3

# Defining the ratio of ages in the hypothesis
arun_age_hypothesis = 5
deepak_age_hypothesis = 3

# Checking if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
if arun_age_premise/arun_age_hypothesis == deepak_age_premise/deepak_age_hypothesis:
    label = "entailment"
else:
    label = "contradiction"
    
print(label)

