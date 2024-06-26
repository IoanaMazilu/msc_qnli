problems_solved_premise = 70
problems_solved_hypothesis = 30

# the hypothesis refers to the range of problems solved by Andy, which is also mentioned in the premise
if problems_solved_hypothesis > problems_solved_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
