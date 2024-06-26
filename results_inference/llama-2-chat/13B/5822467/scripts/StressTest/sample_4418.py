jerry_avg_premise = 80
jerry_avg_hypothesis = 85
fourth_test_score_premise = 70

# the hypothesis refers to the score needed to raise Jerry's average by 5 points
if jerry_avg_hypothesis - jerry_avg_premise > 5:
    # the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif fourth_test_score_premise == jerry_avg_hypothesis:
    # the hypothesis value is consistent with the premise estimate
    label = "entailment"
else:
    # the premise estimate is not sufficient to infer the score needed to raise Jerry's average by 5 points
    label = "neutral"

print(label)
