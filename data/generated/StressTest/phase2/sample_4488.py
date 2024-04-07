# Premise: Sakshi can do a piece of work in 20 days.
# Hypothesis: Sakshi can do a piece of work in less than 80 days.
# Golden Label: entailment

work_time_premise = 20
work_time_hypothesis = 80

# the hypothesis refers to the time Sakshi takes to do a piece of work, which is also mentioned in the premise
if work_time_hypothesis < work_time_premise:
    # check if the hypothesis time contradicts the time specified in the premise
    label = "contradiction"
elif work_time_hypothesis == work_time_premise:
    # if the hypothesis time is equal to the premise time, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis time is more than the premise time, it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

