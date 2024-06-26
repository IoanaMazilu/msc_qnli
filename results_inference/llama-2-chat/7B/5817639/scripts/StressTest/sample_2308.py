speed_premise = 5
speed_hypothesis = 3

# the hypothesis talks about Anne's speed being doubled, referenced in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than'speed_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it would take to clean the house with the current speed, and the hypothesis provides a new estimate that is lower than the premise
    label = "entailment"

print(label)
