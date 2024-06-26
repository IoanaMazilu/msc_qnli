toy_cars_premise = 50.0
additional_cars_premise = 12.0
total_cars_hypothesis = 65.0

# compute the total number of cars in the premise
total_cars_premise = toy_cars_premise + additional_cars_premise

if total_cars_hypothesis > total_cars_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif total_cars_hypothesis < total_cars_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise have the same value, no inference can be made
    label = "neutral"

print(label)
