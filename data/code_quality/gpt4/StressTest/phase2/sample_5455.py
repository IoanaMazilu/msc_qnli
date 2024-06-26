gain_weight_leo_premise = 20
gain_weight_leo_hypothesis = 10

# the hypothesis is about the weight that Leo gains, which is also referenced in the premise
if gain_weight_leo_hypothesis >= gain_weight_leo_premise:
    # check if the weight gain in the hypothesis contradicts the premise's maximum estimated weight gain
    label = "contradiction"
elif gain_weight_leo_hypothesis < gain_weight_leo_premise:
    # if Leo gains less weight than the maximum estimated in the premise, it doesn't contradict the premise but is also not directly entailed by it
    label = "neutral"

print(label)
