price_car_premise = 2
price_ac_premise = 2

# define variables with representative names for the numerical entities in both inputs
price_car_hypothesis = 3
price_ac_hypothesis = 2

# extract all quantities as valid numbers (integers or floats)
price_car_ratio_premise = price_car_premise / price_ac_premise
price_car_ratio_hypothesis = price_car_hypothesis / price_ac_hypothesis

# compare the ratios
if price_car_ratio_hypothesis > price_car_ratio_premise:
    # the hypothesis ratio is greater than the premise ratio, entailment
    label = "entailment"
elif price_car_ratio_hypothesis < price_car_ratio_premise:
    # the hypothesis ratio is less than the premise ratio, contradiction
    label = "contradiction"
else:
    # the hypothesis ratio is equal to the premise ratio, neutral
    label = "neutral"

print(label)
