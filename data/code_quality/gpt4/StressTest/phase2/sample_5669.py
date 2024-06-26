join_time_premise = 2
join_time_hypothesis = 3

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if join_time_premise != join_time_hypothesis:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
