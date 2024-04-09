# define variables with representative names for the numerical entities in both inputs
bean_counts_premise = {
    "Aaron": <7>,
    "Bianca": 7,
    "Callie": 8,
    "Dante": <13>
}

bean_counts_hypothesis = {
    "Aaron": 5,
    "Bianca": 7,
    "Callie": 8,
    "Dante": 13
}

# extract all quantities as valid numbers (integers or floats)
for name, count in bean_counts_premise.items():
    if not isinstance(count, (int, float)):
        raise ValueError("Invalid quantity: {}".format(count))

for name, count in bean_counts_hypothesis.items():
    if not isinstance(count, (int, float)):
        raise ValueError("Invalid quantity: {}".format(count))

# compare the variables
if bean_counts_hypothesis["Aaron"] <= bean_counts_premise["Aaron"]:
    # check if the estimate of 'bean_counts_hypothesis["Aaron"]' contradicts the number of jelly beans in the premise
    label = "contradiction"
elif bean_counts_hypothesis["Bianca"]!= bean_counts_premise["Bianca"]:
    # check if the number of jelly beans in the hypothesis for Bianca contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif bean_counts_hypothesis["Callie"]!= bean_counts_premise["Callie"]:
    # check if the number of jelly beans in the hypothesis for Callie contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif bean_counts_hypothesis["Dante"] <= bean_counts_premise["Dante"]:
    # check if the estimate of 'bean_counts_hypothesis["Dante"]' contradicts the number of jelly beans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
