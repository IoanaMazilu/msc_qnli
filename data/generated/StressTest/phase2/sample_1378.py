# Premise: If Bob runs at a constant rate of more than 6 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Hypothesis: If Bob runs at a constant rate of 8 minutes per mile, how many miles farther south can he run and still be able to return to the parking lot in 50 minutes?
# Golden Label: neutral

running_rate_premise = 6
running_rate_hypothesis = 8
total_time = 50

# the hypothesis refers to Bob's running rate and the total time, mentioned also in the premise
if running_rate_hypothesis <= running_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'running_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Bob's running rate
    # any running rate greater than 'running_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

