# Premise: On his way back, James drives 60 miles per hour and stops in Town B which is midway between Town A and Town C.
# Hypothesis: On his way back, James drives 80 miles per hour and stops in Town B which is midway between Town A and Town C.
# Golden Label: contradiction

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

