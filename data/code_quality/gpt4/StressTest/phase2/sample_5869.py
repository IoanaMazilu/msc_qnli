speed_premise = 51
speed_hypothesis = 31

# the hypothesis talks about Ed's driving speed, referenced also in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
