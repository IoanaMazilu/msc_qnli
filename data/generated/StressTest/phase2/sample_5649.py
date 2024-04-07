# Premise: Carina has 115 ounces of coffee divided into 5-and 10-ounce packages.
# Hypothesis: Carina has less than 815 ounces of coffee divided into 5-and 10-ounce packages.
# Golden Label: entailment

coffee_premise = 115
coffee_hypothesis = 815

# the hypothesis refers to the total amount of coffee Carina has, which is also stated in the premise
if coffee_premise >= coffee_hypothesis:
    # check if the total amount of coffee Carina has in the premise contradicts the estimate of less than 'coffee_hypothesis'
    label = "contradiction"
elif coffee_premise < coffee_hypothesis:
    # if the amount of coffee Carina has in the premise is less than 'coffee_hypothesis', we can infer entailment
    label = "entailment"
else:
    # in the unlikely case that the premise value equals 'coffee_hypothesis'
    label = "neutral"

print(label)

