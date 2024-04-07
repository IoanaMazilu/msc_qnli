# Premise: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is less than 8 times Mary’s age and 4 times as old as Betty.
# Golden Label: entailment

# The premise and hypothesis mention Albert's age in relation to Mary's and Betty's
# The premise and hypothesis don't mention their actual ages

# From the premise
albert_mary_ratio_premise = 2
albert_betty_ratio_premise = 4

# From the hypothesis
albert_mary_ratio_hypothesis = 8
albert_betty_ratio_hypothesis = 4

# check if the ratio of Albert's age to Mary's contradicts the premise
if albert_mary_ratio_hypothesis <= albert_mary_ratio_premise:
    label = "contradiction"
# check if the ratio of Albert's age to Betty's contradicts the premise
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

