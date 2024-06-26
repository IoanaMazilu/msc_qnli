test_count_premise = 4
average_score_premise = 78
test_count_hypothesis = 2
average_score_hypothesis = 78

# the hypothesis refers to the average test score of Ravi mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif test_count_hypothesis != test_count_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
