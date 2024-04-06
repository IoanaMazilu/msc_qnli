# Premise: Olmert was found guilty of breach of trust, but was acquitted on two corruption-related charges.
# Hypothesis: He is convicted of breach of trust and acquitted on two corruption-related charges.
# Golden Label: entailment

guilty_charges_premise = 1
acquitted_charges_premise = 2
guilty_charges_hypothesis = 1
acquitted_charges_hypothesis = 2

# the hypothesis mentions the number of charges for which the person was found guilty and acquitted, which are also mentioned in the premise
if guilty_charges_hypothesis != guilty_charges_premise:
    # check if the number of guilty charges in the hypothesis contradicts the number of guilty charges reported in the premise
    label = "contradiction"
elif acquitted_charges_hypothesis != acquitted_charges_premise:
    # check if the number of acquitted charges from the hypothesis contradicts the number of acquitted charges in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

