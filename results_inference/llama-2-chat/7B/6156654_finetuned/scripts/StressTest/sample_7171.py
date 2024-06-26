problems_solved_premise = 30 to 125
problems_solved_hypothesis = 70 to 125

# the hypothesis refers to the range of problems solved by Andy, which is also mentioned in the premise
if problems_solved_hypothesis >= problems_solved_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif problems_solved_hypothesis < problems_solved_premise:
    # if the hypothesis value is less than the premise value, it is a possibility
    # but not a contradiction, so we can't infer entailment or neutrality
    label = "neutral"
else:
    # if the hypothesis value matches the premise value, it is a possibility
    # but not a contradiction, so we can't infer entailment or neutrality
    label = "neutral"

print(label)
