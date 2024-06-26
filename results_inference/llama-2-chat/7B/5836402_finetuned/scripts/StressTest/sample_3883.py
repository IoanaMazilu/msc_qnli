jogging_time_premise = 4
jogging_time_hypothesis = 3

# the hypothesis refers to the total jogging time, which is also mentioned in the premise
if jogging_time_hypothesis > jogging_time_premise:
    # check if the estimate of 'jogging_time_hypothesis' contradicts the total jogging time in the premise
    label = "contradiction"
elif jogging_time_hypothesis < jogging_time_premise:
    # check if the total jogging time in the hypothesis contradicts the total jogging time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
