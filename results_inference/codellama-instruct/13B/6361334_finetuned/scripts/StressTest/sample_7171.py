problems_solved_premise = 30
problems_solved_hypothesis = 70

# the hypothesis refers to the number of problems solved in a Math exercise, mentioned in the premise
if problems_solved_hypothesis <= problems_solved_premise:
    # check if the estimate of 'problems_solved_hypothesis' contradicts the number of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
