problems_solved_premise = 125
problems_solved_hypothesis = 30

# the hypothesis refers to the range of problems solved by Andy in the premise
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the hypothesis value contradicts the estimate of more than 'problems_solved_premise'
    label = "contradiction"
else:
    # any number of problems solved greater than 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
