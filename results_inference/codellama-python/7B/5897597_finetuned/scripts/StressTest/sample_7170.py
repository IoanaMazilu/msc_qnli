problems_solved_start_premise = 70
problems_solved_end_premise = 125
problems_solved_start_hypothesis = 30
problems_solved_end_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_start_premise < problems_solved_start_hypothesis or problems_solved_end_premise!= problems_solved_end_hypothesis:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
