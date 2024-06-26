premise = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%?"
hypothesis = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 10%?"

# extract the numerical entities from the premise and hypothesis
premise_flights = 3
hypothesis_flights = 3
premise_rate = 50
hypothesis_rate = 10

# check if the hypothesis rate is lower than the premise rate
if hypothesis_rate < premise_rate:
    # check if the number of flights in the hypothesis is greater than the number of flights in the premise
    if hypothesis_flights > premise_flights:
        # the hypothesis is contradictory to the premise
        label = "contradiction"
    else:
        # the hypothesis is neutral to the premise
        label = "neutral"
else:
    # the hypothesis rate is higher than or equal to the premise rate
    # the hypothesis is entailed by the premise
    label = "entailment"

print(label)
