problems_start_premise = 70
problems_end_premise = 125
problems_start_hypothesis = 30
problems_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy, referenced also in the premise
if problems_start_hypothesis > problems_start_premise or problems_end_hypothesis < problems_end_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)