# Premise: Henry completes a piece of work in more than 440 days, Rose completes the same work in 960 days.
# Hypothesis: Henry completes a piece of work in 640 days, Rose completes the same work in 960 days.
# Golden Label: neutral

henry_days_premise = 440
henry_days_hypothesis = 640
rose_days_premise = 960
rose_days_hypothesis = 960

# the hypothesis refers to the number of days Henry and Rose take to complete a task, as mentioned in the premise
if henry_days_hypothesis <= henry_days_premise:
    # check if 'henry_days_hypothesis' contradicts the estimate of more than 'henry_days_premise' days
    label = "contradiction"
elif rose_days_hypothesis != rose_days_premise:
    # check if the number of days Rose takes to complete the task in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Henry takes to complete a task
    # 'henry_days_hypothesis' is greater than 'henry_days_premise' so it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

