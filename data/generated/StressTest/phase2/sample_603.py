# Premise: Bhavan travelled for 20 hours.
# Hypothesis: Bhavan travelled for less than 70 hours.
# Golden Label: entailment

travel_time_premise = 20
travel_time_hypothesis = 70

# the hypothesis talks about the travel time of Bhavan, also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the travel time stated in the premise
    label = "contradiction"
elif travel_time_premise >= travel_time_hypothesis:
    # check if the premise travel time is more than or equal to the hypothesis value
    label = "contradiction"
else:
    # the premise gives an exact time for travel
    # any time less than 'travel_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

