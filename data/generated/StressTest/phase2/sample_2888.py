# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Hypothesis: Mary selects a total of 50 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Golden Label: contradiction

total_fruits_premise = 10
average_price_premise = 52
total_fruits_hypothesis = 50
average_price_hypothesis = 52

# the hypothesis refers to the number of fruits and their average price mentioned in the premise
if total_fruits_premise != total_fruits_hypothesis:
    # check if the total number of fruits selected in the hypothesis contradicts the total number of fruits mentioned in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price of fruits in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

