# Premise: If Ed is 120 km away from Flora at 6 am, and also 120 km away from Flora at 11 am, then how fast is Flora driving (in kilometers per hour)?
# Hypothesis: If Ed is less than 620 km away from Flora at 6 am, and also 120 km away from Flora at 11 am, then how fast is Flora driving (in kilometers per hour)?
# Golden Label: entailment

distance_flora_ed_6am_premise = 120
distance_flora_ed_11am_premise = 120
distance_flora_ed_6am_hypothesis = 620
distance_flora_ed_11am_hypothesis = 120

# the hypothesis refers to the distances between Ed and Flora at specific times mentioned in the premise
if distance_flora_ed_6am_hypothesis < distance_flora_ed_6am_premise:
    # check if the hypothesis estimate contradicts the distance reported in the premise
    label = "contradiction"
elif distance_flora_ed_11am_hypothesis != distance_flora_ed_11am_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates and values do not contradict the premise ones,
    # they cannot be explicitly entailed from the premise either because they are not equal to the premise values
    label = "neutral"

print(label)

