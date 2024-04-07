# Premise: If Ed is less than 620 km away from Flora at 6 am, and also 120 km away from Flora at 11 am, then how fast is Flora driving (in kilometers per hour)?
# Hypothesis: If Ed is 120 km away from Flora at 6 am, and also 120 km away from Flora at 11 am, then how fast is Flora driving (in kilometers per hour)?
# Golden Label: neutral

ed_distance_premise_6am = 620
ed_distance_hypothesis_6am = 120
ed_distance_11am = 120

# the hypothesis talks about the distance of Ed from Flora at specific times, which are also referenced in the premise
if ed_distance_hypothesis_6am > ed_distance_premise_6am:
    # check if the distance in hypothesis at 6 am contradicts the distance in premise at 6 am
    label = "contradiction"
elif ed_distance_hypothesis_6am < ed_distance_premise_6am:
    # check if the distance in hypothesis at 6 am is less than the distance in premise at 6 am
    label = "entailment"
else:
    # if the distance values in hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

