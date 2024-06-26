work_completion_time_premise = 8
work_completion_time_hypothesis = 7

# the hypothesis talks about the time taken to complete the work, which is also mentioned in the premise
if work_completion_time_premise <= work_completion_time_hypothesis:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
