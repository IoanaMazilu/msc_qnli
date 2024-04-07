# Premise: Mary selects a total of less than 30 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Hypothesis: Mary selects a total of 10 apples and oranges from the food stand, and the average (arithmetic mean) price of the 10 pieces of fruit is 52 ¢.
# Golden Label: neutral

fruit_total_premise = 30
fruit_total_hypothesis = 10
average_price_premise = 52
average_price_hypothesis = 52

# the hypothesis refers to the total number of selected fruits and their average price mentioned in the premise
if fruit_total_hypothesis >= fruit_total_premise:
    # check if the total number of fruits in the hypothesis contradicts the estimate of less than 'fruit_total_premise'
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

