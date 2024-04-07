# Premise: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Hypothesis: Alok ordered 86 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Golden Label: contradiction

chapatis_ordered_premise = 16
chapatis_ordered_hypothesis = 86
rice_plates_premise = 5
rice_plates_hypothesis = 5
vegetable_plates_premise = 7
vegetable_plates_hypothesis = 7
ice_cream_cups_premise = 6
ice_cream_cups_hypothesis = 6

# the hypothesis refers to the number of chapatis, plates of rice, plates of mixed vegetable and ice-cream cups mentioned in the premise
if chapatis_ordered_hypothesis != chapatis_ordered_premise:
    # check if the number of chapatis ordered in the hypothesis contradicts the number of chapatis ordered reported in the premise
    label = "contradiction"
elif rice_plates_hypothesis != rice_plates_premise:
    # check if the number of rice plates in the hypothesis contradicts the number of rice plates reported in the premise
    label = "contradiction"
elif vegetable_plates_hypothesis != vegetable_plates_premise:
    # check if the number of vegetable plates in the hypothesis contradicts the number of vegetable plates reported in the premise
    label = "contradiction"
elif ice_cream_cups_hypothesis != ice_cream_cups_premise:
    # check if the number of ice-cream cups in the hypothesis contradicts the number of ice-cream cups reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

