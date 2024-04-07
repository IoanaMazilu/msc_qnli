# Premise: Alok ordered less than 66 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Hypothesis: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Golden Label: neutral

chapatis_premise = 66
chapatis_hypothesis = 16
rice_plates_premise = 5
rice_plates_hypothesis = 5
mixed_veg_plates_premise = 7
mixed_veg_plates_hypothesis = 7
ice_cream_cups_premise = 6
ice_cream_cups_hypothesis = 6

# the hypothesis refers to the number of chapatis, rice plates, mixed vegetable plates and ice cream cups mentioned in the premise
if chapatis_hypothesis >= chapatis_premise:
    # check if the number of chapatis in the hypothesis contradicts the estimate of less than 'chapatis_premise'
    label = "contradiction"
elif rice_plates_hypothesis != rice_plates_premise or mixed_veg_plates_hypothesis != mixed_veg_plates_premise or ice_cream_cups_hypothesis != ice_cream_cups_premise:
    # check if the number of rice plates, mixed vegetable plates or ice cream cups in the hypothesis contradicts the respective numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

