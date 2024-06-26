sheep_horses_ratio_premise = 1 / 7
sheep_horses_ratio_hypothesis = 6 / 7
total_food_premise = 12880
total_food_hypothesis = 12880

# the hypothesis talks about the ratio of sheep to horses, and the total food needed, which are also mentioned in the premise
if sheep_horses_ratio_hypothesis <= sheep_horses_ratio_premise:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
elif total_food_hypothesis!= total_food_premise:
    # check if the total food needed in the hypothesis contradicts the total food needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
