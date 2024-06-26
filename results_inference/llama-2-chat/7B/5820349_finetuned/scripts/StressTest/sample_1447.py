death_rate_premise = 4
death_rate_hypothesis = 5
fearful_departure_rate_premise = 15
fearful_departure_rate_hypothesis = 15

# the hypothesis refers to the death rate and the rate of people leaving due to fear in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the estimate of more than 'death_rate_premise'
    label = "contradiction"
elif fearful_departure_rate_hypothesis!= fearful_departure_rate_premise:
    # check if the rate of people leaving due to fear in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the death rate
    # any death rate greater than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
