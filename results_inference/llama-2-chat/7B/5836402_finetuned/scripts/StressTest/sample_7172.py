problems_solved_premise = range(70, 126)
problems_solved_hypothesis = range(40, 125)

# the hypothesis refers to the range of problems solved by Andy in a Math exercise, which is also mentioned in the premise
if problems_solved_hypothesis >= problems_solved_premise:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_solved_hypothesis < problems_solved_premise:
    # check if the range of problems solved in the hypothesis is less than the range of problems solved in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
