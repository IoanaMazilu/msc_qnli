# Premise: Mary selects a total of less than 50 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: neutral

total_fruit_premise = 50
total_fruit_hypothesis = 10
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis refers to the total number of selected fruits and their average price mentioned in the premise
if total_fruit_hypothesis > total_fruit_premise:
    # check if the total number of fruits in the hypothesis contradicts the estimate of less than 'total_fruit_premise' in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price stated in the premise
    label = "contradiction"
elif total_fruit_hypothesis < total_fruit_premise:
    # the premise gives only an estimate for the total number of fruits
    # any number of fruits less than 'total_fruit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, and total number of fruits is equal, we can infer entailment
    label = "entailment"

print(label)

