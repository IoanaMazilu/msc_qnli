borrowed_amount_premise = 6000
borrowed_amount_hypothesis = 7000

# The hypothesis talks about a total borrowed amount, mentioned also in the premise
if borrowed_amount_hypothesis != borrowed_amount_premise:
    # Check if the borrowed amount in the hypothesis contradicts the borrowed amount in the premise
    label = "contradiction"
else:
    # If the borrowed amounts are the same, we can infer entailment
    label = "entailment"

print(label)
