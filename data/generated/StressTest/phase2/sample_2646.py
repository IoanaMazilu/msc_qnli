# Premise: Sakshi can do a piece of work in 20 days.
# Hypothesis: Sakshi can do a piece of work in less than 70 days.
# Golden Label: entailment

work_time_premise = 20
work_time_hypothesis = 70

# the hypothesis refers to the time Sakshi needs to do a piece of work, mentioned also in the premise
if work_time_hypothesis < work_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
elif work_time_hypothesis == work_time_premise:
    # if the hypothesis time and premise time are equal, we can infer entailment
    label = "entailment"
else:
    # any time less than 'work_time_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

