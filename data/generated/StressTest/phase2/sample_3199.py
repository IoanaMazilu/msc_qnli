# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than less than 80%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 40%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: neutral

on_time_rate_premise = 80
on_time_rate_hypothesis = 40

# the hypothesis refers to the same scenario as the premise, but with a different on-time departure rate
if on_time_rate_premise != on_time_rate_hypothesis:
    # check if the on-time departure rate in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
else:
    # if the on-time departure rate in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

