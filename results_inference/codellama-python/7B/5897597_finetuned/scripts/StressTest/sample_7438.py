fastest_horses_premise = 4
fastest_horses_hypothesis = 3
total_horses = 25

# the hypothesis talks about the number of fastest horses in the London Racetrack, referenced also in the premise
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fastest_horses_premise'
    label = "contradiction"
elif fastest_horses_hypothesis < fastest_horses_premise:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses less than 'fastest_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
