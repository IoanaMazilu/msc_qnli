priya_ratio_premise = 4
priya_ratio_hypothesis = 2

# the hypothesis refers to the ratio of money Priya gets, which is also mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the ratio value in the hypothesis contradicts the estimate of less than 'priya_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'priya_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
