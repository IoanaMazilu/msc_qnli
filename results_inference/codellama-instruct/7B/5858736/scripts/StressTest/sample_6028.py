# the hypothesis talks about the number of tests and the average score, referenced also in the premise
if num_tests_hypothesis <= num_tests_premise:
    # check if the hypothesis value contradicts the estimate of less than 'num_tests_premise'
    label = "contradiction"
elif avg_score_hypothesis!= avg_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
