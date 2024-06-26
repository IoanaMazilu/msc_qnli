problem_start_premise = 30
problem_end_premise = 125
problem_start_hypothesis = 70
problem_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy, which is also mentioned in the premise
if problem_start_hypothesis < problem_start_premise or problem_end_hypothesis!= problem_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems reported in the premise
    label = "contradiction"
elif problem_start_hypothesis > problem_start_premise and problem_end_hypothesis == problem_end_premise:
    # check if the range of problems in the hypothesis is within the range of problems reported in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
