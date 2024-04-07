# Premise: Carina has 55 ounces of coffee divided into 5-and 10-ounce packages.
# Hypothesis: Carina has less than 55 ounces of coffee divided into 5-and 10-ounce packages.
# Golden Label: contradiction

coffee_ounces_premise = 55
coffee_ounces_hypothesis = 55

# the hypothesis refers to the total number of coffee ounces mentioned in the premise
if coffee_ounces_hypothesis >= coffee_ounces_premise:
    # check if 'coffee_ounces_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

