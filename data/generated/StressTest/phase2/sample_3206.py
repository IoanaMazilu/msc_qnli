# Premise: Andy solves problems 75 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems 25 to 125 inclusive in a Math exercise.
# Golden Label: contradiction

problems_start_premise = 75
problems_end_premise = 125
problems_start_hypothesis = 25
problems_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy, also mentioned in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis != problems_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems reported in the premise
    label = "contradiction"
elif problems_start_hypothesis >= problems_start_premise and problems_end_hypothesis == problems_end_premise:
    # if the range of problems in the hypothesis matches the range of problems in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but also cannot be fully entailed from the premise, we infer a neutral relation
    label = "neutral"

print(label)

