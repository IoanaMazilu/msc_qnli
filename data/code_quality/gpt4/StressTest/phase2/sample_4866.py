chapatis_ordered_premise = 16
chapatis_ordered_hypothesis = 36
rice_plates_ordered_premise = 5
rice_plates_ordered_hypothesis = 5
mixed_vegetable_plates_ordered_premise = 7
mixed_vegetable_plates_ordered_hypothesis = 7
ice_cream_cups_ordered_premise = 6
ice_cream_cups_ordered_hypothesis = 6

# the hypothesis provides an estimate for the number of chapatis ordered by Alok, mentioned also in the premise
if chapatis_ordered_premise >= chapatis_ordered_hypothesis:
    # check if the hypothesis value contradicts the number of chapatis ordered by Alok in the premise
    label = "contradiction"
elif rice_plates_ordered_premise != rice_plates_ordered_hypothesis or mixed_vegetable_plates_ordered_premise != mixed_vegetable_plates_ordered_hypothesis or ice_cream_cups_ordered_premise != ice_cream_cups_ordered_hypothesis:
    # check if the number of rice plates, mixed vegetable plates or ice cream cups in the hypothesis contradicts the corresponding number ordered by Alok in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
