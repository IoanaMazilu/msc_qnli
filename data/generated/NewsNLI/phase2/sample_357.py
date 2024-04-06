# Premise: The plan could send nearly 3,000 troops, another U.S. military official familiar with the proposal said.
# Hypothesis: Plan could send nearly 3,000 troops, source says.
# Golden Label: entailment

troops_premise = 3000
troops_hypothesis = 3000

# the hypothesis mentions the number of troops related to a plan, which is also mentioned in the premise
if troops_hypothesis != troops_premise:
    # check if the number of troops in the hypothesis contradicts the number of troops in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

