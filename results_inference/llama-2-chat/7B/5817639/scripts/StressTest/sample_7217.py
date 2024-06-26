truck_fuel_premise = 60
truck_fuel_hypothesis = 10

# the hypothesis talks about the fuel tank capacity of a truck, which is also referenced in the premise
if truck_fuel_hypothesis <= truck_fuel_premise:
    # check if the hypothesis value contradicts the estimate of 'truck_fuel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity of a truck
    # any fuel tank capacity greater than 'truck_fuel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
