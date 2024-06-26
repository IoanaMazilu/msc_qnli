trip_home_premise = 7/2
trip_beach_premise = 7/2
trip_home_hypothesis = 1/2
trip_beach_hypothesis = 1/2

# the hypothesis refers to the time difference between the trip home and the trip to the beach
# the premise mentions the time difference in terms of a ratio, but the hypothesis mentions it in terms of a difference
if trip_home_hypothesis!= trip_beach_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
