henry_work_time_premise = 640
rose_work_time_premise = 960
henry_work_time_hypothesis = 340
rose_work_time_hypothesis = 960

# The hypothesis talks about the time taken by Henry and Rose to complete the work, referenced also in the premise
if henry_work_time_hypothesis != henry_work_time_premise:
    # Check if the time taken by Henry in the hypothesis contradicts the time taken by Henry in the premise
    label = "contradiction"
elif rose_work_time_hypothesis != rose_work_time_premise:
    # Check if the time taken by Rose in the hypothesis contradicts the time taken by Rose in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, then we can infer entailment
    label = "entailment"

print(label)
