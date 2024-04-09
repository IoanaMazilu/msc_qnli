jerry_average_premise = 80
jerry_average_hypothesis = 86
fourth_test_score_premise = 70

# the hypothesis refers to the score needed to raise Jerry's average by less than 6 points
if fourth_test_score_premise <= jerry_average_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif jerry_average_hypothesis - fourth_test_score_premise > 6:
    # check if the difference between the hypothesis value and the premise value is greater than 6
    label = "entailment"
else:
    # the premise gives only an estimate for the score needed to raise Jerry's average
    # any score greater than the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
