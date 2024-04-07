# Premise: Speed of Bruce is 30 m/s and that of Bhishma is 20 m/s.
# Hypothesis: Speed of Bruce is 60 m/s and that of Bhishma is 20 m/s.
# Golden Label: contradiction

speed_bruce_premise = 30
speed_bruce_hypothesis = 60
speed_bhishma_premise = 20
speed_bhishma_hypothesis = 20

# the hypothesis refers to the speeds of Bruce and Bhishma mentioned in the premise
if speed_bruce_premise != speed_bruce_hypothesis:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce reported in the premise
    label = "contradiction"
elif speed_bhishma_premise != speed_bhishma_hypothesis:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)

