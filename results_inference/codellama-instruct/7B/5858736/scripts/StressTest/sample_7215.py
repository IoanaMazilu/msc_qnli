truck_fuel_premise = 60
truck_fuel_hypothesis = 20
distance_travelled = 480

# the hypothesis refers to the number of gallons of fuel used by the truck, referenced also in the premise
if truck_fuel_hypothesis <= truck_fuel_premise:
    # check if the estimate of 'truck_fuel_hypothesis' contradicts the number of gallons of fuel used in the premise
    label = "contradiction"
elif distance_travelled > truck_fuel_premise:
    # check if the distance travelled is greater than the number of gallons of fuel used in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
