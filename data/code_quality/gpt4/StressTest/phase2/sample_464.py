amount_borrowed_premise = 5700
amount_borrowed_hypothesis = 7700

# the hypothesis talks about the total amount borrowed by Albert, also mentioned in the premise
if amount_borrowed_hypothesis != amount_borrowed_premise:
    # check if the total amount borrowed in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise amounts are equal, we can infer entailment
    label = "entailment"

print(label)
