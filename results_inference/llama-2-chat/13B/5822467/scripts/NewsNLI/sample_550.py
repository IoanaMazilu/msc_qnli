width_premise = 4.0
weight_premise = 4000.0
brightness_premise = 5.0

width_hypothesis = 4.0
weight_hypothesis = 4000.0
brightness_hypothesis = 5.0

# the hypothesis mentions the same width, weight, and brightness as the premise
if width_hypothesis == width_premise and weight_hypothesis == weight_premise and brightness_hypothesis == brightness_premise:
    # the hypothesis does not contradict the premise, so the label is neutral
    label = "neutral"
else:
    # if any of the values in the hypothesis contradict the premise values, the label is contradiction
    label = "contradiction"

print(label)
