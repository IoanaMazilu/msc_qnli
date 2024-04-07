# Premise: John completes a piece of work in more than 120 days, Rose completes the same work in 480 days.
# Hypothesis: John completes a piece of work in 320 days, Rose completes the same work in 480 days.
# Golden Label: neutral

john_work_duration_premise = 120
john_work_duration_hypothesis = 320
rose_work_duration_premise = 480
rose_work_duration_hypothesis = 480

# the hypothesis refers to the work durations of John and Rose mentioned in the premise
if john_work_duration_hypothesis <= john_work_duration_premise:
    # check if the estimated 'john_work_duration_hypothesis' contradicts the duration of John's work in the premise
    label = "contradiction"
elif rose_work_duration_hypothesis != rose_work_duration_premise:
    # check if the duration of Rose's work in the hypothesis contradicts the duration of Rose's work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

