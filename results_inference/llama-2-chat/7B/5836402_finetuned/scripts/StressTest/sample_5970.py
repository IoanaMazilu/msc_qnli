seconds_run_premise = 7
seconds_run_hypothesis = 6

# the hypothesis refers to the time Henry took to run the second leg of the course mentioned in the premise
if seconds_run_hypothesis >= seconds_run_premise:
    # check if the hypothesis value contradicts the estimate of less than'seconds_run_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is not possible to infer entailment
    label = "neutral"

print(label)
