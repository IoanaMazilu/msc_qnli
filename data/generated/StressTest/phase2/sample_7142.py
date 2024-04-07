# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 10%?
# Golden Label: contradiction

departure_rate_premise = 50
departure_rate_hypothesis = 10

# the hypothesis refers to the on-time departure rate from the Phoenix airport mentioned in the premise
if departure_rate_premise < departure_rate_hypothesis:
    # check if the 'departure_rate_hypothesis' contradicts the on-time departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis != departure_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

