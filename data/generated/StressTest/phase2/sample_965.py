# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of 20 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: contradiction

total_fruits_premise = 10
total_fruits_hypothesis = 20
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis refers to the total number of fruits selected and the average price of these fruits mentioned in the premise
if total_fruits_premise != total_fruits_hypothesis:
    # check if the total number of fruits in the hypothesis contradicts the total number of fruits reported in the premise
    label = "contradiction"
elif average_price_premise != average_price_hypothesis:
    # check if the average price of fruits in the hypothesis contradicts the average price of fruits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

