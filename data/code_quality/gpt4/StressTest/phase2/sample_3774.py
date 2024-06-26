hotel_xyz_preference_premise = 55
hotel_xyz_preference_hypothesis = 65
hotel_abc_preference_premise = 45
hotel_abc_preference_hypothesis = 45

# the hypothesis refers to the percentage of sales representatives that prefer to stay at Hotel XYZ and Hotel ABC, mentioned also in the premise
if hotel_xyz_preference_hypothesis <= hotel_xyz_preference_premise:
    # check if the estimate of 'hotel_xyz_preference_hypothesis' contradicts the percentage of sales representatives that prefer to stay at Hotel XYZ in the premise
    label = "contradiction"
elif hotel_abc_preference_hypothesis != hotel_abc_preference_premise:
    # check if the percentage of sales representatives that prefer to stay at Hotel ABC in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
