tests_premise = 4
tests_hypothesis = 6
average_score_premise = 50
average_score_hypothesis = 50

# the hypothesis refers to the average test score and the number of tests mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif tests_hypothesis <= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
