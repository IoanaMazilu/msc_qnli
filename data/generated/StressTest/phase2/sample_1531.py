# Premise: Kiran travels from A to B by car and returns from B to A by cycle in more than 6 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Golden Label: neutral

travel_time_premise = 6
travel_time_hypothesis = 7

# the hypothesis talks about the travel time from A to B and back, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time greater than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

