chapatis_ordered_premise = 16
chapatis_ordered_hypothesis = 76
rice_plates_premise = 5
rice_plates_hypothesis = 5
vegetable_plates_premise = 7
vegetable_plates_hypothesis = 7
ice_cream_cups_premise = 5
ice_cream_cups_hypothesis = 5

# the hypothesis refers to the number of chapatis, plates of rice, plates of mixed vegetable and ice cream cups ordered by Alok, mentioned in the premise
if chapatis_ordered_hypothesis != chapatis_ordered_premise:
    # check if the number of chapatis ordered in the hypothesis contradicts the number of chapatis ordered in the premise
    label = "contradiction"
elif rice_plates_hypothesis != rice_plates_premise or vegetable_plates_hypothesis != vegetable_plates_premise or ice_cream_cups_hypothesis != ice_cream_cups_premise:
    # check if the number of rice plates, mixed vegetable plates or ice cream cups in the hypothesis contradicts the number of each reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
