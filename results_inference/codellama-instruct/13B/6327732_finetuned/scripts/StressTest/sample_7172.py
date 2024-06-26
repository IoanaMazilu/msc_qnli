problems_solved_premise = 70
problems_solved_hypothesis = 40

# the hypothesis refers to the range of problems solved by Andy
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the hypothesis value contradicts the estimate of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the range of problems solved
    # any range of problems greater than 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
