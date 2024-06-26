travel_time_premise = 7
travel_time_hypothesis = 7

# the hypothesis refers to the travel time from A to B and back, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact travel time
    # any travel time greater than 'travel_time_premise' contradicts the premise
    label = "contradiction"

print(label)
