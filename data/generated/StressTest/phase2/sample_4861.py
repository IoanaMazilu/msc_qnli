# Premise: Albert is less than 8 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Golden Label: neutral

albert_mary_ratio_premise = 8
albert_mary_ratio_hypothesis = 2
albert_betty_ratio_premise = 4
albert_betty_ratio_hypothesis = 4

# The hypothesis refers to the age ratio of Albert to Mary and Betty's ages which are also mentioned in the premise
if albert_mary_ratio_hypothesis >= albert_mary_ratio_premise:
    # Check if the age ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    # Check if the age ratio of Albert to Betty in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # If the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

