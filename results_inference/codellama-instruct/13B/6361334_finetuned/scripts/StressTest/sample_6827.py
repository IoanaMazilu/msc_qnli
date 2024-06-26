age_ratio_premise = 4/3
age_ratio_hypothesis = 1/3

# the hypothesis refers to the ratio between the ages of Arun and Deepak, mentioned in the premise
if age_ratio_hypothesis!= age_ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact value for the age ratio
    # any value of the age ratio that is consistent with the premise is entailed from the premise
    label = "entailment"

print(label)
