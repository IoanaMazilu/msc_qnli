test_scores_premise = [45, 45, 45, 45]
test_scores_hypothesis = [45, 45, 45, 45, 45]

# the hypothesis refers to the number of tests taken by Joe, which is also mentioned in the premise
if len(test_scores_hypothesis) >= 3:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif sum(test_scores_hypothesis)!= sum(test_scores_premise):
    # check if the total score of the tests in the hypothesis contradicts the total score of the tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
