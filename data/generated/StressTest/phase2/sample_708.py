# Premise: Paul completes a piece of work in 80 days, Rose completes the same work in 120 days.
# Hypothesis: Paul completes a piece of work in more than 70 days, Rose completes the same work in 120 days.
# Golden Label: entailment

paul_work_days_premise = 80
paul_work_days_hypothesis = 70
rose_work_days_premise = 120
rose_work_days_hypothesis = 120

# the hypothesis refers to the work days of Paul and Rose mentioned in the premise
if paul_work_days_premise <= paul_work_days_hypothesis:
    # check if the estimate of 'paul_work_days_hypothesis' contradicts the number of days Paul needs in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days Rose needs in the hypothesis contradicts the number of days Rose needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

