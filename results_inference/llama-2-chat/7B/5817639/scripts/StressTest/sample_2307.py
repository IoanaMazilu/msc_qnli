speed_premise = 2
speed_hypothesis = 1

# the hypothesis talks about Anne's speed being doubled, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for Anne's speed, which the hypothesis does not contradict
    label = "neutral"

print(label)
