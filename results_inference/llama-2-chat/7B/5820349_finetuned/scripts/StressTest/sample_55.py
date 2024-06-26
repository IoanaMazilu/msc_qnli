bruce_speed_premise = 60
bruce_speed_hypothesis = 30
bhishma_speed_premise = 20
bhishma_speed_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, referenced also in the premise
if bruce_speed_hypothesis >= bruce_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bruce_speed_premise'
    label = "contradiction"
elif bhishma_speed_hypothesis!= bhishma_speed_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Bruce
    # any speed of Bruce less than 'bruce_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
