truck_fuel_premise = 20
truck_fuel_hypothesis = 60
distance_travelled = 480

if truck_fuel_hypothesis <= truck_fuel_premise:
    label = "contradiction"
elif distance_travelled % truck_fuel_hypothesis == 0:
    label = "entailment"
else:
    label = "neutral"

print(label)
