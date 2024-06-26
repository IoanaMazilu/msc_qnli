ratio_premise = 1.1428571428571429
ratio_hypothesis = 6.0

# the hypothesis talks about the ratio between the number of sheep and the number of horses at the farm
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the number of sheep and the number of horses
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
