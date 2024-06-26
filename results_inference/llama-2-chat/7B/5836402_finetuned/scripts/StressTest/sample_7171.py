problems_premise = 30
problems_hypothesis = 70

# the hypothesis refers to the number of problems Andy solves in a Math exercise, which is also mentioned in the premise
if problems_hypothesis >= problems_premise:
    # check if the estimate of 'problems_hypothesis' contradicts the range of problems in the premise
    label = "contradiction"
elif problems_hypothesis < problems_premise:
    # check if the estimate of 'problems_hypothesis' is less than the minimum number of problems in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
