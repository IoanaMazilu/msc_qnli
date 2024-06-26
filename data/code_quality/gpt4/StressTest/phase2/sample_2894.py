join_time_premise = 2
join_time_hypothesis = 2

# the hypothesis refers to the time Jose joined mentioned in the premise
if join_time_hypothesis >= join_time_premise:
    # check if the 'join_time_hypothesis' contradicts the time Jose joined in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
