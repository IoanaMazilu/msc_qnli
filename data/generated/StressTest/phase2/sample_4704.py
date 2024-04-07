# Premise: The total price of a kilogram each of Shimla apples and Red Delicious apples is 250 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Hypothesis: The total price of a kilogram each of Shimla apples and Red Delicious apples is less than 350 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Golden Label: entailment

price_difference_premise = 250
price_difference_hypothesis = 350

# the hypothesis talks about the price difference between the same quantities of apples, referenced also in the premise
if price_difference_hypothesis < price_difference_premise:
    # check if the hypothesis value contradicts the value of 'price_difference_premise'
    label = "contradiction"
elif price_difference_hypothesis > price_difference_premise:
    # any price difference greater than 'price_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and premise value are the same, we can infer entailment
    label = "entailment"

print(label)

