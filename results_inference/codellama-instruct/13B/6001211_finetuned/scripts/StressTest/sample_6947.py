travel_time_premise = 7
travel_time_hypothesis = 7

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the exact travel time in the premise
    label = "contradiction"
else:
    # the premise gives the exact travel time
    # any travel time greater than 'travel_time_premise' contradicts the premise
    label = "contradiction"

print(label)