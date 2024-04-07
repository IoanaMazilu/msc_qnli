# Premise: John purchased more than 3 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: John purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: neutral

grapes_kg_premise = 3
grapes_kg_hypothesis = 8
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
grape_rate = 70
mango_rate = 55

# the hypothesis talks about the quantity of grapes and mangoes bought by John, also mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesized quantity of grapes contradicts the premise's estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the hypothesized quantity of mangoes contradicts the exact quantity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of grapes
    # any quantity of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

