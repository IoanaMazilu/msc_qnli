# Define variables for the numerical entities in the premise and hypothesis
petrol_expense_premise = 0.3
house_rent_expense_premise = 0.12
food_expense_premise = 1 - (petrol_expense_premise + house_rent_expense_premise)

petrol_expense_hypothesis = 0.8
house_rent_expense_hypothesis = 0.12
food_expense_hypothesis = 1 - (petrol_expense_hypothesis + house_rent_expense_hypothesis)

# Check if the hypothesis values contradict the premise
if petrol_expense_hypothesis > petrol_expense_premise:
    label = "contradiction"
elif house_rent_expense_hypothesis > house_rent_expense_premise:
    label = "contradiction"
elif food_expense_hypothesis < food_expense_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
