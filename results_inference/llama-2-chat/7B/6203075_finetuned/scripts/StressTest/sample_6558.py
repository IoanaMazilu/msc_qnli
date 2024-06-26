average_score_premise = 78
tests_premise = 3
tests_hypothesis = 6

# the hypothesis refers to the same average score and number of tests mentioned in the premise
if average_score_premise!= average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
