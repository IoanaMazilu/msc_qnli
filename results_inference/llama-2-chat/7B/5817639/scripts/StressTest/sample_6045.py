fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_to_cleveland = 480

# the hypothesis talks about the fuel tank capacity, which is relevant to the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of 'fuel_tank_premise'
    label = "contradiction"
elif distance_to_cleveland <= fuel_tank_hypothesis:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
