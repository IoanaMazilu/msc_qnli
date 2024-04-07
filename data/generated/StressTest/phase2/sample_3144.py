# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 30%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: entailment

on_time_rate_premise = 50
on_time_rate_hypothesis = 30

# the hypothesis refers to the on-time departure rate mentioned in the premise
if on_time_rate_hypothesis >= on_time_rate_premise:
    # check if the 'on_time_rate_hypothesis' contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

