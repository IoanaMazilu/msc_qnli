# Premise: If the trip home took less than 6/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Hypothesis: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Golden Label: neutral

trip_home_premise = 6/2
trip_home_hypothesis = 1/2

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_premise' hours
    label = "contradiction"
elif trip_home_hypothesis < trip_home_premise:
    # any duration less than 'trip_home_premise' hours is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

