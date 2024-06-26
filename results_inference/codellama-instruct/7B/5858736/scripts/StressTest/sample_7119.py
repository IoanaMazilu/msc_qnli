# Define variables for the premise and hypothesis
price_car_premise = 3
price_ac_premise = 2
price_car_hypothesis = 2
price_ac_hypothesis = 2

# Check if the ratio of the premise is greater than or equal to the ratio of the hypothesis
if price_car_premise / price_ac_premise >= price_car_hypothesis / price_ac_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
