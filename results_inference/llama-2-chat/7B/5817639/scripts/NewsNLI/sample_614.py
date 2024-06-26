killed_premise = 5
killed_hypothesis = 5
injured_premise = 4
injured_hypothesis = 3

# compare the number of killed and injured in the hypothesis to the premise
if killed_hypothesis!= killed_premise or injured_hypothesis!= injured_premise:
    # if the number of killed or injured in the hypothesis contradicts the premise, label it as "contradiction"
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise, label it as "entailment"
    label = "entailment"

print(label)
