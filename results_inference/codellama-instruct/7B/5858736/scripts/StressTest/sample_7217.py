truck_fuel_premise = 60
truck_fuel_hypothesis = 10
distance_premise = 480
distance_hypothesis = 480

# the hypothesis talks about the fuel capacity of the truck and the distance to travel
if truck_fuel_hypothesis <= truck_fuel_premise:
    # check if the hypothesis value contradicts the estimate of more than 'truck_fuel_premise'
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance to travel in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
