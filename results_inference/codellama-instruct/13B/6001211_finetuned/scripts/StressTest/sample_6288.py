kiwi_fruit_kg_premise = 8
kiwi_fruit_kg_hypothesis = 5
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the quantity of kiwi fruit bought by Smitha, mentioned also in the premise
if kiwi_fruit_kg_premise <= kiwi_fruit_kg_hypothesis:
    # check if the estimate of 'kiwi_fruit_kg_hypothesis' contradicts the quantity of kiwi fruit bought in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
