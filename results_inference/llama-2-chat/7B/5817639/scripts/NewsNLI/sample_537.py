worth_premise = 1000000
worth_hypothesis = 1000000

# check if the value of the hypothesis contradicts the premise
if worth_hypothesis!= worth_premise:
    label = "contradiction"
else:
    # if the values of the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
