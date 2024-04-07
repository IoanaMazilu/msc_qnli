# Premise: In a locality, the prevailing price of a less than 800 square feet property last year was US Dollar 1000.
# Hypothesis: In a locality, the prevailing price of a 700 square feet property last year was US Dollar 1000.
# Golden Label: neutral

property_size_premise = 800
property_price_premise = 1000
property_size_hypothesis = 700
property_price_hypothesis = 1000

# the hypothesis talks about the property price for a specific size, also referenced in the premise
if property_size_hypothesis >= property_size_premise:
    # check if the property size in the hypothesis contradicts the premise
    label = "contradiction"
elif property_price_hypothesis != property_price_premise:
    # check if the price in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

