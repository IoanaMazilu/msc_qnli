average_score_premise = 60
tests_premise = 4

average_score_hypothesis = 60
tests_hypothesis = 4

# the hypothesis refers to the average score of Joe across more than 4 tests
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif tests_hypothesis > tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
