henry_work_days_premise = 640
henry_work_days_hypothesis = 440
rose_work_days_premise = 960
rose_work_days_hypothesis = 960

# the hypothesis refers to the number of work days of Henry and Rose mentioned in the premise
if henry_work_days_premise <= henry_work_days_hypothesis:
    # check if the estimate of 'henry_work_days_hypothesis' contradicts the number of work days of Henry in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of work days of Rose in the hypothesis contradicts the number of work days of Rose reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
