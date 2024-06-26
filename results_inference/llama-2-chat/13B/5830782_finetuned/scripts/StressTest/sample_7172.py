problem_start_premise = 70
problem_end_premise = 125
problem_start_hypothesis = 40
problem_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problem_start_hypothesis < problem_start_premise or problem_end_hypothesis!= problem_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems reported in the premise
    label = "contradiction"
elif problem_start_hypothesis > problem_start_premise:
    # check if the range of problems in the hypothesis is larger than the range of problems reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)