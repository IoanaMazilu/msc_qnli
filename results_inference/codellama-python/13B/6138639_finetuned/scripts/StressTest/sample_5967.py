dawson_run_premise = 38
dawson_run_hypothesis = 28

# the hypothesis refers to the time Dawson runs the first leg of the course mentioned in the premise
if dawson_run_premise <= dawson_run_hypothesis:
    # check if the estimate of 'dawson_run_hypothesis' contradicts the time Dawson runs the first leg in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)