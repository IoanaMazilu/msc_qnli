cleaning_time_premise = 4
cleaning_time_hypothesis = 1

# the hypothesis refers to the cleaning time of Bruce and Anne mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the estimate of 'cleaning_time_hypothesis' contradicts the cleaning time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
