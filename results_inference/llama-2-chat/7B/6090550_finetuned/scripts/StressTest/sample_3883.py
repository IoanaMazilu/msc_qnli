jogging_time_premise = 4
jogging_time_hypothesis = 3

# the hypothesis refers to the total jogging time, which is also mentioned in the premise
if jogging_time_hypothesis >= jogging_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jogging_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total jogging time
    # any jogging time less than 'jogging_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
