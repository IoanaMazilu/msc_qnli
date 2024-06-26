premise = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%?"
hypothesis = "If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 20%?"

# extract the numerical entities from the premise and hypothesis
premise_num_flights = int(premise.split(" ")[-1])
hypothesis_num_flights = int(hypothesis.split(" ")[-1])

# check if the hypothesis value contradicts the premise value
if hypothesis_num_flights <= premise_num_flights:
    label = "contradiction"
else:
    label = "neutral"

print(label)
