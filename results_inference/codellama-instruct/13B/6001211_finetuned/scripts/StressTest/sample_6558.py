tests_premise = 3
tests_hypothesis = 6
average_score_premise = 78
average_score_hypothesis = 78

# the hypothesis refers to the average score and number of tests mentioned in the premise
if tests_premise >= tests_hypothesis:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)