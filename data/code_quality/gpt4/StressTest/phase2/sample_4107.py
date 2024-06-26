tickets_premise = 10
tickets_hypothesis = 20

# the hypothesis refers to the number of concert tickets bought by Martin, mentioned also in the premise
if tickets_hypothesis <= tickets_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets bought in the premise
    label = "contradiction"
elif tickets_hypothesis > tickets_premise:
    # the premise gives the exact number of tickets
    # any number of tickets less than 'tickets_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
