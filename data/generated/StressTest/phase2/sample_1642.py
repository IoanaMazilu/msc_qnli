# Premise: Alok ordered less than 66 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 5 ice-cream cups.
# Hypothesis: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 5 ice-cream cups.
# Golden Label: neutral

chapatis_ordered_premise = 66
chapatis_ordered_hypothesis = 16
rice_plates_premise = 5
rice_plates_hypothesis = 5
mixed_veg_plates_premise = 7
mixed_veg_plates_hypothesis = 7
ice_cream_cups_premise = 5
ice_cream_cups_hypothesis = 5

# the hypothesis refers to the number of ordered items mentioned in the premise
if chapatis_ordered_hypothesis >= chapatis_ordered_premise:
    # check if the count of 'chapatis_ordered_hypothesis' contradicts the estimation of less than 'chapatis_ordered_premise' chapatis
    label = "contradiction"
elif rice_plates_premise != rice_plates_hypothesis or mixed_veg_plates_premise != mixed_veg_plates_hypothesis or ice_cream_cups_premise != ice_cream_cups_hypothesis:
    # check if the count of other items in the hypothesis contradicts the count of items reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

