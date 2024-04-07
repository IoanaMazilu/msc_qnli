# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 40%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 40%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: contradiction

departure_rate_premise = 40
departure_rate_hypothesis = 40

flights_premise = 3
flights_hypothesis = 3

# the hypothesis refers to the departure rate and number of flights mentioned in the premise
if departure_rate_premise != departure_rate_hypothesis:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
elif flights_premise != flights_hypothesis:
    # check if the number of flights in the hypothesis contradicts the number of flights reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

