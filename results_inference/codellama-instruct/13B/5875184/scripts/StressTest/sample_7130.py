premise = "Anup was asked to find the value of 7/12 of a sum of money T."
hypothesis = "Anup was asked to find the value of more than 7/12 of a sum of money T."

# extract the numerical entities from the premise and hypothesis
premise_value = float(premise.split(" ")[-1])
hypothesis_value = float(hypothesis.split(" ")[-1])

# compare the values
if hypothesis_value > premise_value:
    label = "entailment"
elif hypothesis_value == premise_value:
    label = "neutral"
else:
    label = "contradiction"

print(label)
