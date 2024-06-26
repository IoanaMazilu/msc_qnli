problems_start_premise = 70
problems_end_premise = 125
problems_start_hypothesis = 40
problems_end_hypothesis = 125

# the hypothesis refers to the range of problems Andy solves in a Math exercise, which is also mentioned in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis > problems_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems in the premise
    label = "contradiction"
elif problems_start_hypothesis > problems_start_premise or problems_end_hypothesis < problems_end_premise:
    # check if the range of problems in the hypothesis is not fully included in the range of problems in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
