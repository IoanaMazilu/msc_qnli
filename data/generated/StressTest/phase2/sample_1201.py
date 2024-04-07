# Premise: Kiran travels from A to B by car and returns from B to A by cycle in more than 5 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Golden Label: neutral

travel_time_premise = 5
travel_time_hypothesis = 7

# the hypothesis states the total time of Kiran's travel, also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the time in the hypothesis contradicts the estimate of more than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any time greater than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

