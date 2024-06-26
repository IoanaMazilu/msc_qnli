premise = "George's car calls for 8 ounces of oil for each cylinder used."
hypothesis = "George's car calls for more than 7 ounces of oil for each cylinder used."

# extract the numerical entities from the premise and hypothesis
premise_cylinders = int(premise.split(" ")[-1])
premise_oil = float(premise.split(" ")[-3])
hypothesis_cylinders = int(hypothesis.split(" ")[-1])
hypothesis_oil = float(hypothesis.split(" ")[-3])

# check if the hypothesis value contradicts the premise value
if hypothesis_oil > premise_oil:
    label = "contradiction"
# check if the hypothesis value is consistent with the premise value
elif hypothesis_oil <= premise_oil:
    label = "entailment"
# if the hypothesis value is not consistent with the premise value, we can infer neutrality
else:
    label = "neutral"

print(label)
