# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of less than 40 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: entailment

total_fruits_premise = 10
total_fruits_hypothesis = 40
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis refers to the total number of selected fruits and their average price, both mentioned in the premise
if total_fruits_premise > total_fruits_hypothesis:
    # check if the number of total fruits in the premise contradicts the hypothetical number of fruits
    label = "contradiction"
elif average_price_premise != average_price_hypothesis:
    # check if the average price in the premise contradicts the hypothetical average price
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but the number of selected fruits does not fully entail from the premise
    label = "neutral"

print(label)

