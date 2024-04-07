# Premise: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Hypothesis: Alok ordered less than 86 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Golden Label: entailment

chapatis_ordered_premise = 16
chapatis_ordered_hypothesis = 86
rice_plates_ordered_premise = 5
rice_plates_ordered_hypothesis = 5
mixed_vegetable_plates_ordered_premise = 7
mixed_vegetable_plates_ordered_hypothesis = 7
ice_cream_cups_ordered_premise = 6
ice_cream_cups_ordered_hypothesis = 6

# the hypothesis talks about the number of chapatis, plates of rice, mixed vegetable and ice-cream cups ordered, referenced also in the premise
if chapatis_ordered_hypothesis < chapatis_ordered_premise:
    # check if the hypothesis value contradicts the number of chapatis ordered in the premise
    label = "contradiction"
elif rice_plates_ordered_hypothesis != rice_plates_ordered_premise:
    # check if the number of rice plates in the hypothesis contradicts the number of rice plates ordered in the premise
    label = "contradiction"
elif mixed_vegetable_plates_ordered_hypothesis != mixed_vegetable_plates_ordered_premise:
    # check if the number of mixed vegetable plates in the hypothesis contradicts the number of mixed vegetable plates ordered in the premise
    label = "contradiction"
elif ice_cream_cups_ordered_hypothesis != ice_cream_cups_ordered_premise:
    # check if the number of ice-cream cups in the hypothesis contradicts the number of ice-cream cups ordered in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

