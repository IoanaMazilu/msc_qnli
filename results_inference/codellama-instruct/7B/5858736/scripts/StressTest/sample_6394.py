car_oil_premise = 7
car_oil_hypothesis = 8

if car_oil_hypothesis <= car_oil_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
