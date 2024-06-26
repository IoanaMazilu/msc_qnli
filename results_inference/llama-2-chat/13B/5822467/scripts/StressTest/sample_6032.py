distance_traveled_premise = 1/2
distance_traveled_hypothesis = 7/2

# the hypothesis refers to the distance traveled in the car trip
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_traveled_premise'
    label = "contradiction"
elif distance_traveled_hypothesis > distance_traveled_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled greater than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
