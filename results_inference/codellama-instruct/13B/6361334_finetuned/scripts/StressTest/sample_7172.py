problems_solved_premise = 70
problems_solved_hypothesis = 40

# the hypothesis refers to the range of problems solved by Andy, which is a subset of the range mentioned in the premise
if problems_solved_hypothesis < problems_solved_premise:
    # check if the hypothesis value contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives a range of problems solved by Andy
    # any range of problems greater than or equal to 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
