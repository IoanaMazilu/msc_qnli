# Premise: Carina has 130 ounces of coffee divided into 5-and 10-ounce packages.
# Hypothesis: Carina has 230 ounces of coffee divided into 5-and 10-ounce packages.
# Golden Label: contradiction

coffee_premise = 130
coffee_hypothesis = 230

# the hypothesis refers to the amount of coffee mentioned in the premise
if coffee_premise != coffee_hypothesis:
    # check if the value of 'coffee_hypothesis' contradicts the amount of coffee in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

