problems_solved_premise_min = 30
problems_solved_premise_max = 125
problems_solved_hypothesis_min = 70
problems_solved_hypothesis_max = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_min < problems_solved_premise_min or problems_solved_hypothesis_max > problems_solved_premise_max:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_solved_hypothesis_min < problems_solved_premise_min or problems_solved_hypothesis_max > problems_solved_premise_max:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives only a range for the number of problems solved
    # any range within the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
