age_ratio_premise = 4/3
age_ratio_hypothesis = 1/3

# the hypothesis refers to the ratio between the ages of Arun and Deepak, mentioned in the premise
if age_ratio_premise!= age_ratio_hypothesis:
    # check if the hypothesis value contradicts the ratio between the ages of Arun and Deepak in the premise
    label = "contradiction"
else:
    # the premise gives an explicit ratio between the ages of Arun and Deepak
    # any ratio between the ages of Arun and Deepak consistent with the premise can be explicitly entailed from the premise
    label = "entailment"

print(label)
