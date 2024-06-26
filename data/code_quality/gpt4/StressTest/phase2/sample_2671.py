parents_premise = 80
parents_hypothesis = 40
committees_premise = 3
committees_hypothesis = 3

# the hypothesis refers to the number of parents and committees mentioned in the premise
if parents_hypothesis >= parents_premise:
    # check if the number of parents in the hypothesis contradicts the less than 'parents_premise' parents in the premise
    label = "contradiction"
elif committees_hypothesis != committees_premise:
    # check if the number of committees in the hypothesis contradicts the at least 'committees_premise' committees in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
