time_jim_stretches_premise = 78
time_jim_stretches_hypothesis = 18
time_cara_runs_premise = time_jim_stretches_premise - time_jim_stretches_hypothesis
time_jim_catches_up_premise = time_cara_runs_premise - time_jim_stretches_hypothesis
time_jim_catches_up_hypothesis = time_cara_runs_premise - time_jim_stretches_hypothesis

# the hypothesis refers to the time it takes Jim to stretch and the time it takes Cara to run
if time_jim_stretches_hypothesis < time_jim_stretches_premise:
    # check if the hypothesis value contradicts the estimate of less than 'time_jim_stretches_premise'
    label = "contradiction"
elif time_cara_runs_hypothesis!= time_cara_runs_premise:
    # check if the hypothesis value contradicts the estimate of how many minutes it takes Cara to run
    label = "contradiction"
elif time_jim_catches_up_hypothesis!= time_jim_catches_up_premise:
    # check if the hypothesis value contradicts the estimate of how many minutes it takes Jim to catch up to Cara
    label = "contradiction"
else:
    # the premise gives only estimates for the time it takes Jim to stretch and the time it takes Cara to run
    # any number of minutes greater than 'time_jim_stretches_premise' and 'time_cara_runs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
