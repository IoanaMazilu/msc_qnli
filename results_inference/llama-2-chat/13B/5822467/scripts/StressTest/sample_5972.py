henry_runs_premise = 7
henry_runs_hypothesis = 6

# the hypothesis refers to the time taken by Henry to run the second leg of the course
if henry_runs_hypothesis <= henry_runs_premise:
    # check if the hypothesis value contradicts the estimate of 'henry_runs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Henry
    # any time taken less than or equal to 'henry_runs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
