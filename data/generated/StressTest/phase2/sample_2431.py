# Premise: Sravan travelled for less than 65 hours.
# Hypothesis: Sravan travelled for 15 hours.
# Golden Label: neutral

travel_time_premise = 65
travel_time_hypothesis = 15

# the hypothesis talks about the duration of travel, referenced also in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time lower than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

