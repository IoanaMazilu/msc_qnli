jim_stretch_time_premise = 78
jim_stretch_time_hypothesis = 18

# the hypothesis refers to the time Jim spends stretching, which is also mentioned in the premise
if jim_stretch_time_hypothesis >= jim_stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jim_stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jim spends stretching
    # any time less than 'jim_stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
