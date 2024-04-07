# Premise: Pavan travelled for less than 61 hours.
# Hypothesis: Pavan travelled for 11 hours.
# Golden Label: neutral

travel_hours_premise = 61
travel_hours_hypothesis = 11

# the hypothesis mentions the number of hours Pavan travelled, which is also mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # if the number of hours in the hypothesis contradicts the premise (less than 'travel_hours_premise')
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel hours
    # any number of hours less than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

