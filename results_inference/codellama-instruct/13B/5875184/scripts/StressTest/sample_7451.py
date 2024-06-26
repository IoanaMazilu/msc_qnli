income_premise = 100
petrol_premise = 30
house_rent_premise = 12
food_premise = 100 - petrol_premise - house_rent_premise

income_hypothesis = 100
petrol_hypothesis = 30
house_rent_hypothesis = 12
food_hypothesis = 100 - petrol_hypothesis - house_rent_hypothesis

if petrol_hypothesis > petrol_premise:
    label = "entailment"
elif petrol_hypothesis < petrol_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
