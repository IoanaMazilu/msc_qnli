problems_solved_premise = 70
problems_solved_hypothesis = 30
problems_solved_inclusive = 125

# the hypothesis refers to the range of problems solved by Andy, which is also mentioned in the premise
if problems_solved_hypothesis >= problems_solved_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif problems_solved_hypothesis < problems_solved_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
