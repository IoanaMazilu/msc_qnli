# Premise: If Leo gains 10 pounds, he will weigh 50% more than his sister Kendra.
# Hypothesis: If Leo gains more than 10 pounds, he will weigh 50% more than his sister Kendra.
# Golden Label: contradiction

weight_gain_premise = 10
weight_gain_hypothesis = 10

# the hypothesis refers to a potential weight gain for Leo, which is also mentioned in the premise
if weight_gain_hypothesis > weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the weight gain mentioned in the premise
    label = "contradiction"
elif weight_gain_hypothesis < weight_gain_premise:
    # check if the weight gain in the hypothesis is less than the weight gain mentioned in the premise
    label = "contradiction"
else:
    # the weight gain in the hypothesis is the same as in the premise,
    # but the hypothesis suggests that it could be more, which is not stated in the premise
    label = "neutral"

print(label)

