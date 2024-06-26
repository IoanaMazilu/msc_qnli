ratio_premise = 4/3
ratio_hypothesis = 6/3
age_premise = 34
age_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio and the age of Rahul
    # any ratio less than 'ratio_premise' and age of 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
