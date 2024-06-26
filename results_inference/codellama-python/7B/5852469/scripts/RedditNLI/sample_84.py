rate_premise = 2.5
rate_hypothesis = 2.5

# the hypothesis and premise mention the same rate of growth
if rate_hypothesis!= rate_premise:
    # check if the rate of growth in the hypothesis contradicts the rate of growth in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same rate of growth
    # however, the hypothesis does not link the rate of growth to any specific aspect of the economy
    label = "neutral"

print(label)
