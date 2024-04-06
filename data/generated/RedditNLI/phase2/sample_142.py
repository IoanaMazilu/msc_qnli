# Premise: Loan Scandal Costs Wells Fargo $1 Billion; None of Fine Goes to Victims-Truthdig.
# Hypothesis: Wells Fargo Said to Be Target of $1 Billion U.S. Fine.
# Golden Label: entailment

fine_premise = 1_000_000_000
fine_hypothesis = 1_000_000_000

# the hypothesis and premise mention the fine Wells Fargo has to pay
if fine_hypothesis != fine_premise:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

