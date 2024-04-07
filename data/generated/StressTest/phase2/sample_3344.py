# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 60%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: contradiction

departure_rate_premise = 60
departure_rate_hypothesis = 60

# the hypothesis is about the on-time departure rate from Phoenix, which is also referenced in the premise
if departure_rate_hypothesis != departure_rate_premise:
    # check if the rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis rate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

