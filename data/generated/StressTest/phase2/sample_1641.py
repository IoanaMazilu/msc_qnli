# Premise: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 5 ice-cream cups.
# Hypothesis: Alok ordered less than 66 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 5 ice-cream cups.
# Golden Label: entailment

chapatis_ordered_premise = 16
chapatis_ordered_hypothesis = 66
rice_plates_ordered_premise = 5
rice_plates_ordered_hypothesis = 5
mixed_vegetable_plates_ordered_premise = 7
mixed_vegetable_plates_ordered_hypothesis = 7
ice_cream_cups_ordered_premise = 5
ice_cream_cups_ordered_hypothesis = 5

# the hypothesis refers to the number of chapatis, rice plates, mixed vegetable plates and ice-cream cups ordered by Alok, mentioned in the premise
if chapatis_ordered_hypothesis <= chapatis_ordered_premise:
    # check if the estimate of 'chapatis_ordered_hypothesis' contradicts the number of chapatis ordered in the premise
    label = "contradiction"
elif rice_plates_ordered_hypothesis != rice_plates_ordered_premise or mixed_vegetable_plates_ordered_hypothesis != mixed_vegetable_plates_ordered_premise or ice_cream_cups_ordered_hypothesis != ice_cream_cups_ordered_premise:
    # check if the number of rice plates, mixed vegetable plates or ice-cream cups ordered in the hypothesis contradicts the number of rice plates, mixed vegetable plates or ice-cream cups ordered in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

