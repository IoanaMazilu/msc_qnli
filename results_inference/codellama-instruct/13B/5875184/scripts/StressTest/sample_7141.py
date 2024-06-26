premise = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 40%?"
hypothesis = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%?"

# extract the numerical entities from the premise and hypothesis
premise_flights = 3
hypothesis_flights = 3
premise_rate = 40
hypothesis_rate = 50

# check if the hypothesis rate is higher than the premise rate
if hypothesis_rate > premise_rate:
    # check if the number of flights in the hypothesis is greater than the number of flights in the premise
    if hypothesis_flights > premise_flights:
        # the hypothesis is more specific than the premise, so it entails the premise
        label = "entailment"
    else:
        # the hypothesis is not more specific than the premise, so it does not entail the premise
        label = "neutral"
else:
    # the hypothesis rate is not higher than the premise rate, so it contradicts the premise
    label = "contradiction"

print(label)
