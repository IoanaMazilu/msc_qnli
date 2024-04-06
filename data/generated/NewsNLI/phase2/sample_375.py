# Premise: And Bud Ice showed 5.35 %, compared with the label's 5.5%.
# Hypothesis: Bud Ice showed 5.35% alcohol by volume compared with the label's 5.5 %.
# Golden Label: entailment

bud_ice_premise = 5.35
label_premise = 5.5
bud_ice_hypothesis = 5.35
label_hypothesis = 5.5

# the hypothesis mentions the percentage of alcohol by volume of Bud Ice and the label, which are also referenced in the premise
if bud_ice_hypothesis != bud_ice_premise:
    # check if the Bud Ice percentage in the hypothesis contradicts the Bud Ice percentage in the premise
    label = "contradiction"
elif label_hypothesis != label_premise:
    # check if the label percentage from the hypothesis contradicts the label percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

