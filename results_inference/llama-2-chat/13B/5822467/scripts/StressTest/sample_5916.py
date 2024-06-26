jerry_avg_premise = 80  # premise: Jerry's current average is 80
jerry_avg_hypothesis = 73  # hypothesis: Jerry wants to raise his average by less than 7 points
fourth_test_score_premise = None  # premise: the score Jerry needs to earn on the fourth test to raise his average by 2 points
fourth_test_score_hypothesis = None  # hypothesis: the score Jerry needs to earn on the fourth test to raise his average by less than 7 points

# define variables with representative names for the numerical entities in both inputs

# extract all quantities as valid numbers (integers or floats)

# compare the variables to infer the label
if jerry_avg_hypothesis > jerry_avg_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif jerry_avg_hypothesis < jerry_avg_premise:
    # the premise contradicts the hypothesis
    label = "contradiction"
elif fourth_test_score_hypothesis is None or fourth_test_score_premise is None:
    # no comparison is needed, the premise and hypothesis do not provide enough information
    label = "neutral"
else:
    # the premise and hypothesis provide enough information to infer the label
    if fourth_test_score_hypothesis > fourth_test_score_premise:
        # the hypothesis entails the premise
        label = "entailment"
    elif fourth_test_score_hypothesis < fourth_test_score_premise:
        # the premise contradicts the hypothesis
        label = "contradiction"
    else:
        # the premise and hypothesis are consistent, but no entailment can be inferred
        label = "neutral"

print(label)
