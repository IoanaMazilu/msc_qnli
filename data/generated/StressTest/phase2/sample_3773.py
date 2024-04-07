# Premise: On a business trip, 30 percent of 60 sales representatives will be given accommodations at Hotel XYZ and the remaining 70 percent will be given accommodations at Hotel ABC.
# Hypothesis: On a business trip, 80 percent of 60 sales representatives will be given accommodations at Hotel XYZ and the remaining 70 percent will be given accommodations at Hotel ABC.
# Golden Label: contradiction

total_representatives = 60
hotel_xyz_premise = 0.3 * total_representatives
hotel_abc_premise = 0.7 * total_representatives
hotel_xyz_hypothesis = 0.8 * total_representatives
hotel_abc_hypothesis = 0.7 * total_representatives

# the hypothesis refers to the number of sales representatives staying at each hotel, mentioned in the premise
if hotel_xyz_premise != hotel_xyz_hypothesis:
    # check if the number of representatives at Hotel XYZ in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif hotel_abc_premise != hotel_abc_hypothesis:
    # check if the number of representatives at Hotel ABC in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

