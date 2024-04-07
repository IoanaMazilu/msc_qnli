# Premise: Bhaman travelled for less than 85 hours.
# Hypothesis: Bhaman travelled for 15 hours.
# Golden Label: neutral

travel_hours_premise = 85
travel_hours_hypothesis = 15

# the hypothesis refers to the number of travel hours mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # check if the travel time in the hypothesis contradicts the estimate of less than 'travel_hours_premise' travel hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel hours
    # any number of travel hours less than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

