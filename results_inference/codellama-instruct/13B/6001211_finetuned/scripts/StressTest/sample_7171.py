problems_solved_min_premise = 30
problems_solved_max_premise = 125
problems_solved_min_hypothesis = 70
problems_solved_max_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_min_hypothesis < problems_solved_min_premise or problems_solved_max_hypothesis > problems_solved_max_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_solved_min_hypothesis > problems_solved_min_premise or problems_solved_max_hypothesis < problems_solved_max_premise:
    # check if the range of problems solved in the hypothesis is within the range of problems solved in the premise
    label = "entailment"
else:
    # if the range of problems solved in the hypothesis is exactly the same as the range of problems solved in the premise, we can infer entailment
    label = "entailment"

print(label)
