# Premise: Pavan travelled for less than 31 hours.
# Hypothesis: Pavan travelled for 11 hours.
# Golden Label: neutral

travel_hours_premise = 31
travel_hours_hypothesis = 11

# The hypothesis talks about the number of hours Pavan travelled, which is also referenced in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # Check if the hypothesis value contradicts the premise value of less than 'travel_hours_premise'
    label = "contradiction"
else:
    # Any number of hours less than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

