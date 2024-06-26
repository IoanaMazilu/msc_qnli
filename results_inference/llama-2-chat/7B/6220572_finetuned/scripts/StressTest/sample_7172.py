problems_solved_premise = 125
problems_solved_hypothesis = 125

# the hypothesis talks about the range of problems solved by Andy, referenced also in the premise
if problems_solved_hypothesis >= problems_solved_premise:
    # check if the hypothesis value contradicts the estimate of less than 'problems_solved_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the range of problems solved
    # any range of problems solved less than 'problems_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
