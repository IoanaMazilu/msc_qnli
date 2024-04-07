# Premise: Albert is less than 5 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Golden Label: neutral

albert_relative_age_premise = 5  # Albert's age relative to Mary's age in the premise
albert_relative_age_hypothesis = 2  # Albert's age relative to Mary's age in the hypothesis
albert_relative_age_betty_premise = 4  # Albert's age relative to Betty's age in the premise
albert_relative_age_betty_hypothesis = 4  # Albert's age relative to Betty's age in the hypothesis

# the hypothesis talks about Albert's age relative to Mary's and Betty's age, referenced also in the premise
if albert_relative_age_hypothesis >= albert_relative_age_premise:
    # check if the hypothesis value contradicts the estimate of Albert's age being less than 'albert_relative_age_premise' times Mary's age
    label = "contradiction"
elif albert_relative_age_betty_hypothesis != albert_relative_age_betty_premise:
    # check if the relative age to Betty in the hypothesis contradicts the relative age to Betty in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

