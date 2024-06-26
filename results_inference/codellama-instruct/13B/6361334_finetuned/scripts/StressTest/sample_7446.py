ratio_premise = 4/3
ratio_hypothesis = 1/3
age_premise = 26
age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
