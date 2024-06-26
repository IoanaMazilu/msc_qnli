tests_premise = 4
tests_hypothesis = 6
average_score_premise = 50
average_score_hypothesis = 50

# the hypothesis refers to the number of tests and the average score reported in the premise
if tests_hypothesis <= tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
