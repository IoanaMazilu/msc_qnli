# Premise: During a car trip, Maria stopped to rest after she traveled less than 5/2 of the total distance to her destination.
# Hypothesis: During a car trip, Maria stopped to rest after she traveled 1/2 of the total distance to her destination.
# Golden Label: neutral

distance_traveled_premise = 5/2
distance_traveled_hypothesis = 1/2

# the hypothesis talks about the distance traveled by Maria during a car trip, also mentioned in the premise
if distance_traveled_hypothesis > distance_traveled_premise:
    # check if the hypothesis value contradicts the estimation of less than 'distance_traveled_premise'
    label = "contradiction"
elif distance_traveled_hypothesis == distance_traveled_premise:
    # check if the hypothesis value contradicts the estimation of less than 'distance_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance less than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

