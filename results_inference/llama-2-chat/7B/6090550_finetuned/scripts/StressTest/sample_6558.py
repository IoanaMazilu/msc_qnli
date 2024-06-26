average_score_premise = 78
tests_taken_premise = 3
tests_taken_hypothesis = 6

# the hypothesis refers to the average score of Jerry on the first 3 tests, which is also mentioned in the premise
if tests_taken_hypothesis < tests_taken_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_premise!= average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
