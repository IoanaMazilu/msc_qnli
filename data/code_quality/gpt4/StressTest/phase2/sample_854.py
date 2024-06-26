first_leg_run_time_premise = 22
first_leg_run_time_hypothesis = 52

# the hypothesis talks about the same event (Paul running the first leg of the course) mentioned in the premise
if first_leg_run_time_hypothesis != first_leg_run_time_premise:
    # check if the time Paul took to run the first leg in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time is the same as the premise time, we can infer entailment
    label = "entailment"

print(label)
