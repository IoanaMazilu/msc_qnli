tests_premise = 3
tests_hypothesis = 3
average_score_premise = 90
average_score_hypothesis = 90

# the hypothesis refers to the average score on the first 'tests_hypothesis' tests mentioned in the premise
if tests_hypothesis > tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
elif average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
