# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than less than 50%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: contradiction

departure_rate_premise = 50
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_premise != departure_rate_hypothesis:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

