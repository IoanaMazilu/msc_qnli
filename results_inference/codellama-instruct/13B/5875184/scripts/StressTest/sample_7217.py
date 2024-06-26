premise_fuel_tank = 60
hypothesis_fuel_tank = 10
premise_distance = 480
hypothesis_distance = 480

# the hypothesis refers to the fuel tank size and distance mentioned in the premise
if hypothesis_fuel_tank <= premise_fuel_tank:
    # check if the estimate of 'hypothesis_fuel_tank' contradicts the number of gallons in the premise
    label = "contradiction"
elif hypothesis_distance!= premise_distance:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
