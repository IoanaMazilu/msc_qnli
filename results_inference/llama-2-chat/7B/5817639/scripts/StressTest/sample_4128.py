# Define variables for the entities in the premise and hypothesis
car_premise = 60
car_hypothesis = 30

# Compare the values of the variables to determine the relation
if car_hypothesis <= car_premise:
    # If the hypothesis value contradicts the premise value, label it as "contradiction"
    label = "contradiction"
elif car_hypothesis > car_premise:
    # If the hypothesis value is greater than the premise value, label it as "entailment"
    label = "entailment"
else:
    # If the hypothesis value is equal to or less than the premise value, label it as "neutral"
    label = "neutral"

print(label)
