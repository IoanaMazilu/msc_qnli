problems_start_premise = 74
problems_end_premise = 135
problems_start_hypothesis = 54
problems_end_hypothesis = 135

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_start_hypothesis < problems_start_premise or problems_end_hypothesis != problems_end_premise:
    # check if the range of problems solved in the hypothesis contradicts the range reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
