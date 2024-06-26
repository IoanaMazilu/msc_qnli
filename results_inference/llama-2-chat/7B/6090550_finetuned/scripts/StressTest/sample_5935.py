y = 60
x = 480

Fuel_tank_premise = 20
Fuel_tank_hypothesis = 60

Fuel_tank_premise_gallons_to_fly_to_Cleveland = 480
Fuel_tank_hypothesis_gallons_to_fly_to_Cleveland = 480

# the hypothesis talks about the fuel tank size of a small aircraft that wants to fly to Cleveland, which is also mentioned in the premise
if Fuel_tank_premise_gallons_to_fly_to_Cleveland!= Fuel_tank_hypothesis_gallons_to_fly_to_Cleveland:
    # check if the number of gallons to fly to Cleveland in the hypothesis contradicts the number of gallons to fly to Cleveland in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
