problems_solved_premise = 70
problems_solved_hypothesis = 30
problems_solved_range_premise = 125
problems_solved_range_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy in the Math exercise mentioned in the premise
if problems_solved_hypothesis < problems_solved_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the number of problems solved in the premise
    label = "contradiction"
elif problems_solved_hypothesis > problems_solved_range_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
