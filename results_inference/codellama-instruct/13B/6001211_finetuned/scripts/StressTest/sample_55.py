speed_bruce_premise = 60
speed_bruce_hypothesis = 30
speed_bhishma_premise = 20
speed_bhishma_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if speed_bruce_hypothesis >= speed_bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce in the premise
    label = "contradiction"
elif speed_bhishma_hypothesis!= speed_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Bruce
    # any speed less than'speed_bruce_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
