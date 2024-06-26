time_premise = 80
time_hypothesis = 40

# the hypothesis also refers to the time Annie stopped to fix a flat tire
if time_hypothesis >= time_premise:
    # check if the hypothesis time contradicts the estimate of less than 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
