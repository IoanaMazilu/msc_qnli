# Premise: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is 3 times Mary’s age and 4 times as old as Betty.
# Golden Label: contradiction

# Defining the variables.
albert_age_multiple_mary_premise = 2
albert_age_multiple_betty_premise = 4
albert_age_multiple_mary_hypothesis = 3
albert_age_multiple_betty_hypothesis = 4

# The hypothesis refers to Albert's age as multiples of Mary's and Betty's ages, which is also mentioned in the premise.
if albert_age_multiple_mary_premise != albert_age_multiple_mary_hypothesis:
    # Check if the multiplier of Mary's age for Albert in the hypothesis contradicts the one in the premise.
    label = "contradiction"
elif albert_age_multiple_betty_premise != albert_age_multiple_betty_hypothesis:
    # Check if the multiplier of Betty's age for Albert in the hypothesis contradicts the one in the premise.
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment.
    label = "entailment"

print(label)

