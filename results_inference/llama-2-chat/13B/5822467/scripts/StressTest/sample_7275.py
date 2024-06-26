molly_max_speed_premise = 100
molly_max_speed_hypothesis = 400

# the hypothesis refers to the speed at which Molly and Max are driving
if molly_max_speed_hypothesis <= molly_max_speed_premise:
    # check if the hypothesis value contradicts the estimate of'molly_max_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed at which Molly and Max are driving
    # any speed less than 400 kilometers per hour is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
