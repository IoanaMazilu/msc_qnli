test_scores_premise = [78, 80, 82, 85]
test_scores_hypothesis = [78, 80, 82]

# the hypothesis refers to the number of tests and the average score, both mentioned in the premise
if len(test_scores_hypothesis) < len(test_scores_premise):
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif sum(test_scores_hypothesis) / len(test_scores_hypothesis)!= sum(test_scores_premise) / len(test_scores_premise):
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
