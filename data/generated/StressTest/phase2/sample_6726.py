# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 56 ¢.
# Hypothesis: Mary selects a total of less than 20 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 56 ¢.
# Golden Label: entailment

total_fruits_premise = 10
total_fruits_hypothesis = 20
average_price_premise = 56
average_price_hypothesis = 56

# the hypothesis refers to the number of fruits and their average price mentioned in the premise
if total_fruits_hypothesis <= total_fruits_premise:
    # check if the estimate of 'total_fruits_hypothesis' contradicts the number of total fruits in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

