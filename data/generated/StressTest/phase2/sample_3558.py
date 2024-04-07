# Premise: Mary completes a piece of work in 160 days, Rose completes the same work in 240 days.
# Hypothesis: Mary completes a piece of work in less than 360 days, Rose completes the same work in 240 days.
# Golden Label: entailment

mary_work_days_premise = 160
rose_work_days_premise = 240
mary_work_days_hypothesis = 360
rose_work_days_hypothesis = 240

# the hypothesis refers to the number of days Mary and Rose need to complete a piece of work mentioned in the premise
if mary_work_days_hypothesis < mary_work_days_premise:
    # check if the estimate of 'mary_work_days_hypothesis' contradicts the number of work days for Mary in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of work days for Rose in the hypothesis contradicts the number of work days reported for Rose in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

