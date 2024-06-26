speed_premise = 60
speed_hypothesis = 80

# The hypothesis refers to the speed of James's driving, as mentioned in the premise
if speed_hypothesis != speed_premise:
    # Check if the speed value in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # The hypothesis and the premise agree on the speed of James's driving
    label = "entailment"

print(label)
