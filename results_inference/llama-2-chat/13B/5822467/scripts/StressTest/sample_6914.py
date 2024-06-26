# define variables with representative names for the numerical entities in both inputs
flight_departure_premise = 3
flight_departure_hypothesis = 3
on_time_departure_rate_premise = 70
on_time_departure_rate_hypothesis = 50

# extract all quantities as valid numbers (integers or floats)
flight_departure_premise = int(flight_departure_premise)
flight_departure_hypothesis = int(flight_departure_hypothesis)
on_time_departure_rate_premise = float(on_time_departure_rate_premise)
on_time_departure_rate_hypothesis = float(on_time_departure_rate_hypothesis)

# use brief comments to explain what comparison we do between the defined variables
# in this case, we compare the on-time departure rate premise with the on-time departure rate hypothesis

# perform calculations if necessary
on_time_departure_rate_diff = on_time_departure_rate_hypothesis - on_time_departure_rate_premise

# compare the results and infer the label
if on_time_departure_rate_diff > 0:
    # the hypothesis on-time departure rate is higher than the premise, so we have entailment
    label = "entailment"
elif on_time_departure_rate_diff == 0:
    # the hypothesis on-time departure rate is the same as the premise, so we have neutrality
    label = "neutral"
else:
    # the hypothesis on-time departure rate is lower than the premise, so we have contradiction
    label = "contradiction"

print(label)
