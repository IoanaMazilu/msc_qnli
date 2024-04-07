# Premise: Mr Yadav spends more than 30% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Hypothesis: Mr Yadav spends 60% of his monthly salary on consumable items and 50% of the remaining on clothes and transport.
# Golden Label: neutral

consumable_items_premise = 0.30
consumable_items_hypothesis = 0.60
clothes_transport_premise = 0.50
clothes_transport_hypothesis = 0.50

# the hypothesis talks about the percentage of salary Mr Yadav spends on consumable items and clothes/transport, also mentioned in the premise
if consumable_items_hypothesis <= consumable_items_premise and clothes_transport_hypothesis == clothes_transport_premise:
    # check if the hypothesis value contradicts the estimate of more than 'consumable_items_premise' or equals 'clothes_transport_premise'
    label = "contradiction"
elif consumable_items_hypothesis > consumable_items_premise and clothes_transport_hypothesis == clothes_transport_premise:
    # the premise gives only an estimate for the percentage of salary spent on consumables
    # any percentage greater than 'consumable_items_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

