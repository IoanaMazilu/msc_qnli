# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Hypothesis: Mary selects a total of less than 30 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Golden Label: entailment

total_fruits_premise = 10
total_fruits_hypothesis = 30
average_price_premise = 52
average_price_hypothesis = 52

# the hypothesis refers to the total number of fruits and their average price, both mentioned in the premise
if total_fruits_hypothesis <= total_fruits_premise:
    # check if the hypothesis value contradicts the total number of selected fruits in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

