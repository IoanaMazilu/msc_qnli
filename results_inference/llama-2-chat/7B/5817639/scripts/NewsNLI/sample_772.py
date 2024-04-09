county_seat_premise = "Hazard"
jobless_rate_premise = 0.127

# extract the values from the hypothesis
unemployment_rate_hypothesis = float(11.1)

# compare the values
if unemployment_rate_hypothesis!= jobless_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the values do not contradict, we can infer entailment
    label = "entailment"

print(label)
