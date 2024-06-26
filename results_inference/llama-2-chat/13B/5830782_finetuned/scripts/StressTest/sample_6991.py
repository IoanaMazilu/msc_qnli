distance_run_premise = 52
distance_run_hypothesis = 12

# the hypothesis talks about the distance the sisters ran, referenced also in the premise
if distance_run_hypothesis >= distance_run_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_run_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance the sisters ran
    # any distance less than 'distance_run_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
