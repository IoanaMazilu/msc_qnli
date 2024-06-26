distance_traveled_premise = 8/2
distance_traveled_hypothesis = 1/2

# the hypothesis talks about the distance Maria traveled during a car trip, referenced also in the premise
if distance_traveled_hypothesis >= distance_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance less than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
