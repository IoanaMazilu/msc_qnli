# Premise: Raman travelled for less than 20 hours.
# Hypothesis: Raman travelled for 10 hours.
# Golden Label: neutral

travel_time_premise = 20
travel_time_hypothesis = 10

# the hypothesis mentions a specific travel time for Raman, which is also referenced in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

