# define variables with representative names for the numerical entities in both inputs
x_premise = 40
x_hypothesis = 50
hourly_wage_premise = x_premise * 2
hourly_wage_hypothesis = x_hypothesis * 2

# extract all quantities as valid numbers (integers or floats)
hourly_wage_premise = int(hourly_wage_premise)
hourly_wage_hypothesis = int(hourly_wage_hypothesis)

# compare the variables
if hourly_wage_premise <= hourly_wage_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
