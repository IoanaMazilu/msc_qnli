# Defining the premise and hypothesis
premise_departure_rate = 60
hypothesis_departure_rate = 20

# The hypothesis refers to the on-time departure rate of the airport, which is also mentioned in the premise
if premise_departure_rate <= hypothesis_departure_rate:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
