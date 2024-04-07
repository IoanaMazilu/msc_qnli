# Premise: If Leo gains less than 30 pounds, he will weigh 50% more than his sister Kendra.
# Hypothesis: If Leo gains 10 pounds, he will weigh 50% more than his sister Kendra.
# Golden Label: neutral

weight_gain_premise = 30
weight_gain_hypothesis = 10

# the hypothesis talks about Leo's weight gain referenced also in the premise
if weight_gain_hypothesis >= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the estimate of less than 'weight_gain_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight gain
    # any weight gain less than 'weight_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

