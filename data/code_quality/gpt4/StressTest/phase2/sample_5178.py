average_score_premise = 95
average_score_hypothesis = 35
number_of_tests = 5

# the hypothesis refers to the average score of Joe's first 5 tests mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the estimate of 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
