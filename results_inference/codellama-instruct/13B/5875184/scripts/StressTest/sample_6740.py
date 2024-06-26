premise = "Diane find 1 can of paint are just enough to paint one third of her room."
hypothesis = "Diane find less than 1 can of paint are just enough to paint one third of her room."

# extract the numerical entities from the premise and hypothesis
premise_can_count = int(premise.split(" ")[2])
hypothesis_can_count = int(hypothesis.split(" ")[2])

# compare the number of cans found in the premise and hypothesis
if premise_can_count > hypothesis_can_count:
    label = "contradiction"
elif premise_can_count < hypothesis_can_count:
    label = "entailment"
else:
    label = "neutral"

print(label)
