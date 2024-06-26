chapatis_ordered_premise = 36
chapatis_ordered_hypothesis = 16
rice_plates_premise = 5
rice_plates_hypothesis = 5
mixed_vegetable_plates_premise = 7
mixed_vegetable_plates_hypothesis = 7
ice_cream_cups_premise = 6
ice_cream_cups_hypothesis = 6

# the hypothesis mentions the same food items and their quantities as in the premise
if chapatis_ordered_hypothesis >= chapatis_ordered_premise:
    # check if the number of chapatis in the hypothesis contradicts the estimate of less than 'chapatis_ordered_premise'
    label = "contradiction"
elif rice_plates_hypothesis != rice_plates_premise or mixed_vegetable_plates_hypothesis != mixed_vegetable_plates_premise or ice_cream_cups_hypothesis != ice_cream_cups_premise:
    # check if the number of plates of rice, mixed vegetables or ice-cream cups in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
