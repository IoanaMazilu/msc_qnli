problems_solved_premise = 70
problems_solved_hypothesis = 30

# the hypothesis refers to the range of problems solved by Andy
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives an inclusive range of problems solved
    # any number of problems greater than 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
