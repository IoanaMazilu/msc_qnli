premise = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 20%?"
hypothesis = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%?"

# extract the numerical entities from the premise and hypothesis
premise_flights = 3
hypothesis_flights = 3
premise_rate = 20
hypothesis_rate = 60

# check if the hypothesis rate is higher than the premise rate
if hypothesis_rate > premise_rate:
    # check if the number of flights in the hypothesis is greater than the number of flights in the premise
    if hypothesis_flights > premise_flights:
        # the hypothesis is more specific than the premise, so we can infer entailment
        label = "entailment"
    else:
        # the hypothesis is not more specific than the premise, so we can infer neutrality
        label = "neutral"
else:
    # the hypothesis rate is not higher than the premise rate, so we can infer contradiction
    label = "contradiction"

print(label)
