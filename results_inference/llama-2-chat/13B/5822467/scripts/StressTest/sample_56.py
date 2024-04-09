bruce_speed_premise = 30
bhishma_speed_premise = 20
bruce_speed_hypothesis = 60
bhishma_speed_hypothesis = 20

# the hypothesis talks about the speeds of Bruce and Bhishma, referenced also in the premise
if bruce_speed_hypothesis > bruce_speed_premise and bhishma_speed_hypothesis > bhishma_speed_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif bruce_speed_hypothesis <= bruce_speed_premise and bhishma_speed_hypothesis <= bhishma_speed_premise:
    # check if the hypothesis values are consistent with the premise values
    label = "neutral"
else:
    # the premise gives only an estimate for the speeds of Bruce and Bhishma
    # any speed greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
