# Premise: Pavan travelled for 11 hours.
# Hypothesis: Pavan travelled for more than 11 hours.
# Golden Label: contradiction

travel_time_premise = 11
travel_time_hypothesis = 11

# the hypothesis refers to the travel time of Pavan mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the exact travel time in the premise
    label = "contradiction"
else:
    # the premise gives the exact travel time
    # any travel time less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

