fastest_horses_premise = 3
fastest_horses_hypothesis = 4

# the hypothesis refers to the number of fastest horses submitted by the London Racetrack
if fastest_horses_hypothesis <= fastest_horses_premise:
    # check if the hypothesis value contradicts the estimate of 'fastest_horses_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses greater than 'fastest_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
