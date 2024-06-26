problems_solved_premise = 70
problems_solved_hypothesis = 40

# the hypothesis refers to a range of problems that includes the range of problems mentioned in the premise
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the number of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of problems solved
    # any number of problems solved greater than 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
