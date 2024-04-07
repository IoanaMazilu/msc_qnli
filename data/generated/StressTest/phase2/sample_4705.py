# Premise: The total price of a kilogram each of Shimla apples and Red Delicious apples is less than 350 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Hypothesis: The total price of a kilogram each of Shimla apples and Red Delicious apples is 250 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Golden Label: neutral

price_difference_premise = 350
price_difference_hypothesis = 250

# the hypothesis refers to the difference in total prices of two pairs of apple varieties, which is also mentioned in the premise
if price_difference_hypothesis >= price_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'price_difference_premise' rupees
    label = "contradiction"
elif price_difference_hypothesis < price_difference_premise:
    # if the hypothesis value is less than 'price_difference_premise', it can be entailed from the premise
    label = "entailment"

print(label)

