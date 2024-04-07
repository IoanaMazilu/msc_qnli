# Premise: John completes a piece of work in 320 days, Rose completes the same work in 480 days.
# Hypothesis: John completes a piece of work in more than 120 days, Rose completes the same work in 480 days.
# Golden Label: entailment

john_work_days_premise = 320
john_work_days_hypothesis = 120
rose_work_days_premise = 480
rose_work_days_hypothesis = 480

# the hypothesis refers to the number of days John and Rose need to complete a work, which are mentioned in the premise
if john_work_days_hypothesis >= john_work_days_premise:
    # check if the estimate of 'john_work_days_hypothesis' contradicts the number of work days for John in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of work days for Rose in the hypothesis contradicts the number of work days for Rose reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

