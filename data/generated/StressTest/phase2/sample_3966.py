# Premise: Albert is 2 times Mary’s age but only 4 times as old as Betty.
# Hypothesis: Albert is less than 7 times Mary’s age but only 4 times as old as Betty.
# Golden Label: entailment

albert_mary_ratio_premise = 2
albert_mary_ratio_hypothesis = 7
albert_betty_ratio_premise = 4
albert_betty_ratio_hypothesis = 4

# the hypothesis refers to the age ratios between Albert, Mary and Betty indicated in the premise
if albert_mary_ratio_hypothesis < albert_mary_ratio_premise:
    # check if the hypothesis value contradicts the 'albert_mary_ratio_premise'
    label = "contradiction"
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    # check if the hypothesis value contradicts the 'albert_betty_ratio_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

