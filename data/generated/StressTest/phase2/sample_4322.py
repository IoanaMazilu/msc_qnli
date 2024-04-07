# Premise: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Hypothesis: Mary selects a total of less than 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 54 ¢.
# Golden Label: contradiction

fruit_total_premise = 10
fruit_total_hypothesis = 10
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis talks about the total number of selected fruits and their average price, both mentioned in the premise
if fruit_total_hypothesis >= fruit_total_premise:
    # check if the estimate of 'fruit_total_hypothesis' contradicts the number of selected fruits in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price of selected fruits in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

