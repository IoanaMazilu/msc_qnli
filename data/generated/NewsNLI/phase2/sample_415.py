# Premise: 42 percent of homeless children are younger than 6.
# Hypothesis: Study says 42 percent of homeless children are younger than 6.
# Golden Label: entailment

percentage_homeless_children_premise = 0.42
percentage_homeless_children_hypothesis = 0.42

# the hypothesis mentions the percentage of homeless children under six, which is also mentioned in the premise
if percentage_homeless_children_hypothesis != percentage_homeless_children_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

