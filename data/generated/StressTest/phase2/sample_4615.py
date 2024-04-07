# Premise: Alok ordered less than 46 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Hypothesis: Alok ordered 16 chapatis, 5 plates of rice, 7 plates of mixed vegetable and 6 ice-cream cups.
# Golden Label: neutral

chapatis_ordered_premise = 46
chapatis_ordered_hypothesis = 16
rice_ordered_premise = 5
rice_ordered_hypothesis = 5
mixed_vegetable_ordered_premise = 7
mixed_vegetable_ordered_hypothesis = 7
ice_cream_cups_ordered_premise = 6
ice_cream_cups_ordered_hypothesis = 6

# the hypothesis refers to the number of chapatis, rice plates, mixed vegetable plates and ice-cream cups ordered by Alok
if chapatis_ordered_hypothesis >= chapatis_ordered_premise:
    # check if the number of chapatis ordered in the hypothesis contradicts the estimate of less than 'chapatis_ordered_premise'
    label = "contradiction"
elif rice_ordered_hypothesis != rice_ordered_premise or mixed_vegetable_ordered_hypothesis != mixed_vegetable_ordered_premise or ice_cream_cups_ordered_hypothesis != ice_cream_cups_ordered_premise:
    # check if the number of rice plates, mixed vegetable plates or ice-cream cups in the hypothesis contradicts the number of them reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

