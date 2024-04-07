# Premise: Andy solves problems 70 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems 40 to 125 inclusive in a Math exercise.
# Golden Label: contradiction

problems_start_premise = 70
problems_end_premise = 125
problems_start_hypothesis = 40
problems_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis != problems_end_premise:
    # check if the start or end of the problems range in the hypothesis contradicts the range of problems in the premise
    label = "contradiction"
elif problems_start_hypothesis != problems_start_premise or problems_end_hypothesis != problems_end_premise:
    # if the problems range in the hypothesis does not contradict the one in the premise but also does not match it exactly
    label = "neutral"
else:
    # if the problems range in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)

