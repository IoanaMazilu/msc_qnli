lists_premise = 2/4
lists_hypothesis = 1/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the number of lists and members mentioned in the premise
if lists_hypothesis >= lists_premise:
    # check if the estimate of 'lists_hypothesis' contradicts the number of lists in the premise
    label = "contradiction"
elif members_hypothesis!= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
