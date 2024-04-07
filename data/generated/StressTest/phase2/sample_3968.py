# Premise: Albert is 2 times Mary’s age but only 4 times as old as Betty.
# Hypothesis: Albert is 6 times Mary’s age but only 4 times as old as Betty.
# Golden Label: contradiction

albert_age_mult_mary_premise = 2
albert_age_mult_mary_hypothesis = 6
albert_age_mult_betty_premise = 4
albert_age_mult_betty_hypothesis = 4

# the hypothesis refers to Albert's age in relation to Mary's and Betty's ages, also mentioned in the premise
if albert_age_mult_mary_premise != albert_age_mult_mary_hypothesis:
    # check if the multiplier of Mary's age to get Albert's age in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif albert_age_mult_betty_premise != albert_age_mult_betty_hypothesis:
    # check if the multiplier of Betty's age to get Albert's age in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

