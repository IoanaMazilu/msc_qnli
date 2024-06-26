ratio_premise = 8/2
ratio_hypothesis = 5/2
age_premise = 26
age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
