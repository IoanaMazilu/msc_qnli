# the hypothesis refers to the ratio of sheep to horses and the number of horses, referenced also in the premise
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the hypothesis value contradicts the ratio of sheep to horses in the premise
    label = "contradiction"
elif horses_fed_per_day_hypothesis!= horses_fed_per_day_premise:
    # check if the number of horses fed per day in the hypothesis contradicts the number of horses fed per day reported in the premise
    label = "contradiction"
elif total_food_needed_hypothesis!= total_food_needed_premise:
    # check if the total food needed in the hypothesis contradicts the total food needed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
