# Premise: The total price of a kilogram each of Shimla apples and Red Delicious apples is 250 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Hypothesis: The total price of a kilogram each of Shimla apples and Red Delicious apples is 650 rupees more than the total price of a kilogram each of Red Delicious apples and Fuji apples.
# Golden Label: contradiction

price_difference_premise = 250
price_difference_hypothesis = 650

# the hypothesis talks about the price difference between a kilogram each of Shimla apples and Red Delicious apples and a kilogram each of Red Delicious apples and Fuji apples, that is also referenced in the premise
if price_difference_premise != price_difference_hypothesis:
    # check if the price difference in the hypothesis contradicts the price difference reported in the premise
    label = "contradiction"
else:
    # if the price differences do not contradict each other, we can infer entailment
    label = "entailment"

print(label)

