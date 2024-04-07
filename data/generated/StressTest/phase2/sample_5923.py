# Premise: If the trip home took less than 3/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?
# Hypothesis: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?
# Golden Label: neutral

trip_to_beach_premise = 1.5
trip_to_beach_hypothesis = 0.5

# the hypothesis talks about the time taken by Carl for his trip to the beach and back home
if trip_to_beach_hypothesis >= trip_to_beach_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'trip_to_beach_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of the trip
    # any time less than 'trip_to_beach_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

