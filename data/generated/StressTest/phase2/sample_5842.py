# Premise: Andy solves problems more than 64 to 135 inclusive in a Math exercise.
# Hypothesis: Andy solves problems 74 to 135 inclusive in a Math exercise.
# Golden Label: neutral

problems_start_premise = 64
problems_end_premise = 135
problems_start_hypothesis = 74
problems_end_hypothesis = 135

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis > problems_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems in the premise
    label = "contradiction"
elif problems_start_hypothesis == problems_start_premise and problems_end_hypothesis == problems_end_premise:
    # check if the range of problems in the hypothesis fully matches the range of problems in the premise
    label = "entailment"
else:
    # if the range of problems in the hypothesis is within the range of problems in the premise,
    # but does not fully match it, we can infer neutrality
    label = "neutral"

print(label)

