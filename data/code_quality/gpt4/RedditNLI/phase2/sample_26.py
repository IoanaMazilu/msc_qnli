amount_premise = 100000
amount_hypothesis = 100000
bonds_premise = 5
bonds_hypothesis = 3

# the hypothesis and premise mention the amount to invest and the number of bonds
if amount_premise != amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif bonds_premise != bonds_hypothesis:
    # check if the number of bonds in the hypothesis contradicts the number of bonds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
