# Premise: For dinner, Cara ate 240 grams of bread which was eight times as much bread as she ate for lunch, and six times as much bread as she ate for breakfast.
# Hypothesis: For dinner, Cara ate more than 140 grams of bread which was eight times as much bread as she ate for lunch, and six times as much bread as she ate for breakfast.
# Golden Label: entailment

bread_dinner_premise = 240
bread_dinner_hypothesis = 140

# the hypothesis refers to the quantity of bread Cara ate for dinner, lunch, and breakfast, mentioned in the premise
if bread_dinner_hypothesis >= bread_dinner_premise:
    # check if the estimate of 'bread_dinner_hypothesis' contradicts the quantity of bread dinner mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact quantity for the bread Cara ate for dinner
    # the hypothesis is consistent with this quantity, so we can infer entailment
    label = "entailment"

print(label)

