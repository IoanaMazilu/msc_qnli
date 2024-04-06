# Premise: U.S. to fine Wells Fargo $1 billion.
# Hypothesis: Wells Fargo Said to Be Target of $1 Billion U.S. Fine.
# Golden Label: entailment

fine_premise = 1 * 10**9
fine_hypothesis = 1 * 10**9

# the hypothesis and premise mention the same fine value
if fine_premise != fine_hypothesis:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "contradiction"
else:
    # if the fine in the hypothesis does not contradict the fine in the premise, we can infer entailment
    label = "entailment"

print(label)

