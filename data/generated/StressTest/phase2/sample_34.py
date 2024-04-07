# Premise: Mr Yadav spends more than 10% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Hypothesis: Mr Yadav spends 60% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Golden Label: neutral

consumable_items_premise = 10
consumable_items_hypothesis = 60
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis talks about the percentage of Mr Yadav's monthly salary spent on consumable items and clothes and transport, also mentioned in the premise
if consumable_items_hypothesis <= consumable_items_premise and clothes_transport_hypothesis == clothes_transport_premise:
    # check if the percentage of salary spent on consumable items and on clothes and transport in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif consumable_items_hypothesis > consumable_items_premise and clothes_transport_hypothesis == clothes_transport_premise:
    # check if the estimate of 'consumable_items_hypothesis' contradicts the percentage of salary spent on consumable items in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

