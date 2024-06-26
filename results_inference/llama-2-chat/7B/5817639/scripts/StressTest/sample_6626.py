ratio_premise = 6
ratio_hypothesis = 7
sheep_premise = 0
horse_food_premise = 12880

# the hypothesis talks about the ratio between sheep and horses, and also refers to the same farm and food needs as the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif sheep_hypothesis!= sheep_premise:
    # check if the number of sheep in the hypothesis contradicts the number of sheep reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
