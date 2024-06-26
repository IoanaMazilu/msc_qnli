problems_solved_lower_premise = 30
problems_solved_upper_premise = 125
problems_solved_lower_hypothesis = 70
problems_solved_upper_hypothesis = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_lower_hypothesis < problems_solved_lower_premise or problems_solved_upper_hypothesis!= problems_solved_upper_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the lower limit of problems solved
    # any number of problems solved in the range of 'problems_solved_lower_hypothesis' to 'problems_solved_upper_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
