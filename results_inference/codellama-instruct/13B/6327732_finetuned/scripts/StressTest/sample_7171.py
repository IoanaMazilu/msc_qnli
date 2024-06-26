problems_solved_premise = 30
problems_solved_hypothesis = 70

# the hypothesis refers to the number of problems solved in a Math exercise, mentioned in the premise
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the number of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of problems solved, but any number of problems solved between 70 and 125 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
