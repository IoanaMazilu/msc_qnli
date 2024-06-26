average_score_premise = 90
tests_taken_premise = 4
tests_considered_hypothesis = 3

# the hypothesis refers to the number of tests considered in the average calculation
if tests_considered_hypothesis <= tests_taken_premise:
    # check if the hypothesis value contradicts the number of tests reported in the premise
    label = "contradiction"
elif average_score_premise!= average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
