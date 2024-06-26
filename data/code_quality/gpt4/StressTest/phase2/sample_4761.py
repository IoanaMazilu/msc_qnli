water_added_premise = 8
water_added_hypothesis = 7
initial_tank_status_premise = 3/4
initial_tank_status_hypothesis = 3/4
final_tank_status_premise = 7/8
final_tank_status_hypothesis = 7/8

# the hypothesis refers to the amount of water added to a tank that is already partially full, mentioned also in the premise
if water_added_hypothesis >= water_added_premise:
    # check if the estimate of 'water_added_hypothesis' contradicts the amount of water added in the premise
    label = "contradiction"
elif initial_tank_status_hypothesis != initial_tank_status_premise:
    # check if the initial tank status in the hypothesis contradicts the initial tank status reported in the premise
    label = "contradiction"
elif final_tank_status_hypothesis != final_tank_status_premise:
    # check if the final tank status in the hypothesis contradicts the final tank status reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
