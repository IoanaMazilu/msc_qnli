# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 56 ¢.
# Hypothesis: Mary selects a total of 20 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 56 ¢.
# Golden Label: contradiction

total_fruit_premise = 10
average_price_premise = 56
total_fruit_hypothesis = 20
average_price_hypothesis = 56

# the hypothesis refers to the total number of fruits and their average price as in the premise
if total_fruit_premise != total_fruit_hypothesis:
    # check if the number of fruits in the hypothesis contradicts the number of fruits mentioned in the premise
    label = "contradiction"
elif average_price_premise != average_price_hypothesis:
    # check if the average price in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

