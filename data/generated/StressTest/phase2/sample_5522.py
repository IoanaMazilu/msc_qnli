# Premise: Dan’s car gets 32 miles per gallon.
# Hypothesis: Dan’s car gets 52 miles per gallon.
# Golden Label: contradiction

car_mileage_premise = 32
car_mileage_hypothesis = 52

# the hypothesis refers to the mileage of Dan's car, as mentioned in the premise
if car_mileage_premise != car_mileage_hypothesis:
    # check if the mileage in the hypothesis contradicts the mileage reported in the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)

