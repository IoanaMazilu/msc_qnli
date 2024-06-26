shares_owned_premise = 2000
shares_owned_hypothesis = 5000

# The hypothesis refers to the number of shares Sam owns, which is also mentioned in the premise
if shares_owned_hypothesis <= shares_owned_premise:
    # Check if the number of shares in the hypothesis contradicts the number of shares in the premise
    label = "contradiction"
else:
    # If the number of shares in the hypothesis does not contradict the number of shares in the premise, we can infer entailment
    label = "entailment"

print(label)
