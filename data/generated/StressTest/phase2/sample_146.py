# Premise: Andy solves problems 78 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems less than 78 to 125 inclusive in a Math exercise.
# Golden Label: contradiction

problems_start_premise = 78
problems_end_premise = 125
problems_start_hypothesis = 78
problems_end_hypothesis = 125

# the hypothesis talks about the range of problems solved by Andy, mentioned also in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis != problems_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_start_hypothesis == problems_start_premise and problems_end_hypothesis == problems_end_premise:
    # if the hypothesis range is equal to the premise range, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis range does not contradict the premise range but is not equal, we infer neutrality
    label = "neutral"

print(label)

