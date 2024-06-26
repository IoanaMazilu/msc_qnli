distance_run_hypothesis = 3

if distance_run_hypothesis <= 2:
    # check if the hypothesis value contradicts the estimate of less than 'distance_run_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance run
    # any distance less than 'distance_run_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
