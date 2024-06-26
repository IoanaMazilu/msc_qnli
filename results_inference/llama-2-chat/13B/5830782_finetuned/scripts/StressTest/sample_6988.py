ratio_premise = 2/3
ratio_hypothesis = 7/3

# the hypothesis refers to the age ratio of Anil and his son, also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any age ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
