henry_runs_premise = 7
henry_runs_hypothesis = 6

# the hypothesis refers to the time it takes Henry to run the second leg of the course
if henry_runs_hypothesis > henry_runs_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif henry_runs_hypothesis == henry_runs_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise gives only an estimate for the time it takes Henry to run the second leg of the course
    # any time greater than 6 seconds is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
