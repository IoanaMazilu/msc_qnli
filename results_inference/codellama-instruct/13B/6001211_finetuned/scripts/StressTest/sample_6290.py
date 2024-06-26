kiwi_fruit_kg_premise = 8
kiwi_fruit_kg_hypothesis = 8
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the quantity of kiwi fruit bought by Smitha, mentioned also in the premise
if kiwi_fruit_kg_hypothesis <= kiwi_fruit_kg_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of kiwi fruit
    # any quantity of kiwi fruit greater than 'kiwi_fruit_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
