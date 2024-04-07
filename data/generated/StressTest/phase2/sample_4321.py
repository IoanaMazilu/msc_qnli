# Premise: Mary selects a total of less than 40 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: neutral

total_fruits_premise = 40
total_fruits_hypothesis = 10
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis refers to the total number of selected fruits and the average price per fruit mentioned in the premise
if total_fruits_hypothesis >= total_fruits_premise:
    # check if the total number of fruits selected in the hypothesis contradicts the estimate of less than 'total_fruits_premise'
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price per fruit in the hypothesis contradicts the average price per fruit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

