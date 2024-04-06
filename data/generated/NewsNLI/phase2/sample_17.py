# Premise: A customer's late arrival cost her an additional $1,116 for her car rental.
# Hypothesis: She was charged an additional $1,116 for the rental because of the late pick up.
# Golden Label: entailment

additional_cost_premise = 1116
additional_cost_hypothesis = 1116

# the hypothesis mentions an additional charge of $1,116 for the rental due to a late pick up, which is also referenced in the premise
if additional_cost_hypothesis != additional_cost_premise:
    # check if the additional cost in the hypothesis contradicts the additional cost reported in the premise
    label = "contradiction"
else:
    # if the additional cost in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

