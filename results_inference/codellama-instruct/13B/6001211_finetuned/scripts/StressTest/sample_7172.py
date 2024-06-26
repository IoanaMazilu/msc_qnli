problems_solved_start_premise = 70
problems_solved_end_premise = 125
problems_solved_start_hypothesis = 40
problems_solved_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_start_hypothesis < problems_solved_start_premise or problems_solved_end_hypothesis!= problems_solved_end_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the range of problems solved in the hypothesis does not contradict the range of problems solved in the premise, we can infer entailment
    label = "entailment"

print(label)
