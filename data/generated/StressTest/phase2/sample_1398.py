# Premise: With the help of Pavan, they completed the work in 8 days and earned Rs.
# Hypothesis: With the help of Pavan, they completed the work in more than 5 days and earned Rs.
# Golden Label: entailment

work_completion_time_premise = 8
work_completion_time_hypothesis = 5

# the hypothesis refers to the time of work completion in the premise
if work_completion_time_premise <= work_completion_time_hypothesis:
    # check if the estimate of 'work_completion_time_hypothesis' contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

