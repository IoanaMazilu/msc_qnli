# Premise: Mary selects a total of less than 80 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: neutral

fruit_selection_premise = 80
fruit_selection_hypothesis = 10
average_price_premise = 0.54
average_price_hypothesis = 0.54

# the hypothesis talks about the number of selected fruits and their average price, both referenced in the premise
if fruit_selection_hypothesis > fruit_selection_premise:
    # check if the number of fruits selected in the hypothesis contradicts the estimate of less than 'fruit_selection_premise' in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

