test_score_premise = 82
test_count_premise = 9
test_score_hypothesis = 82
test_count_hypothesis = 2

# the hypothesis refers to Robin's average test score and the number of tests mentioned in the premise
if test_score_hypothesis!= test_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif test_count_hypothesis >= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)