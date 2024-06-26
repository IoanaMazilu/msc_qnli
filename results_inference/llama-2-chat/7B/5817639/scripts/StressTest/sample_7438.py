racetrack_horses_premise = 25
racetrack_horses_hypothesis = 3

# the hypothesis talks about the number of fastest horses to be submitted by the London Racetrack
if racetrack_horses_hypothesis <= racetrack_horses_premise:
    # check if the hypothesis value contradicts the estimate of less than 'racetrack_horses_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses greater than 'racetrack_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
