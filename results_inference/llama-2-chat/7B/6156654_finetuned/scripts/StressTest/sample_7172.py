problems_solved_premise = 70 to 125
problems_solved_hypothesis = 40 to 125

# the hypothesis refers to the range of problems solved by Andy in the exercise, which is also mentioned in the premise
if problems_solved_hypothesis >= problems_solved_premise:
    # check if the range of problems solved in the hypothesis is greater than or equal to the range of problems solved in the premise
    label = "entailment"
elif problems_solved_hypothesis < problems_solved_premise:
    # check if the range of problems solved in the hypothesis is less than the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
