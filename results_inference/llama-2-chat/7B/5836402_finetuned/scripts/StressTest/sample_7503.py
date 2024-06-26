stop_time_premise = 10
stop_time_hypothesis = 20

# the hypothesis refers to the time Pat stops stretching, mentioned in the premise
if stop_time_premise >= stop_time_hypothesis:
    # check if the premise value contradicts the estimate of less than'stop_time_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
