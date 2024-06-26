chapatis_premise = 86
chapatis_hypothesis = 16
rice_premise = 5
rice_hypothesis = 5
vegetable_premise = 7
vegetable_hypothesis = 7
ice_cream_premise = 6
ice_cream_hypothesis = 6

# The hypothesis talks about the number of chapatis, plates of rice, mixed vegetable and ice-cream cups ordered by Alok, which is also referenced in the premise
if chapatis_hypothesis >= chapatis_premise:
    # Check if the number of chapatis in the hypothesis contradicts the estimate of less than 'chapatis_premise'
    label = "contradiction"
elif rice_hypothesis != rice_premise or vegetable_hypothesis != vegetable_premise or ice_cream_hypothesis != ice_cream_premise:
    # Check if the number of rice plates, mixed vegetable plates or ice-cream cups in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif chapatis_hypothesis > chapatis_premise:
    # Any number of chapatis less than 'chapatis_premise' in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
