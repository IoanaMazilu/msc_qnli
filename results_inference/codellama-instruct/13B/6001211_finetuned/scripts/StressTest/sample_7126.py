jogging_walking_time_premise = 1
jogging_walking_time_hypothesis = 3

# the hypothesis refers to the total time Aaron spends jogging and walking, which is also mentioned in the premise
if jogging_walking_time_hypothesis <= jogging_walking_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jogging_walking_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total time
    # any time greater than 'jogging_walking_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
