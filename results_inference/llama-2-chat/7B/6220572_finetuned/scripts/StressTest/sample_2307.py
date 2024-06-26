doubled_speed_premise = 2
doubled_speed_hypothesis = 5

# the hypothesis refers to the time it would take to clean the house if Anne's speed were doubled, also mentioned in the premise
if doubled_speed_hypothesis <= doubled_speed_premise:
    # check if the estimate of 'doubled_speed_hypothesis' contradicts the time it would take to clean the house if Anne's speed were doubled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it would take to clean the house if Anne's speed were doubled
    # any time less than 'doubled_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
