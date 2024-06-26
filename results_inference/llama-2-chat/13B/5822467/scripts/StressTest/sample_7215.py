fuel_tank_premise = 60
distance_premise = 480
hypothesis_fuel_tank = 20

# the hypothesis talks about the fuel tank capacity, referenced also in the premise
if hypothesis_fuel_tank <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'fuel_tank_premise'
    label = "contradiction"
elif distance_premise > (hypothesis_fuel_tank * 0.8):
    # check if the estimated distance to travel contradicts the hypothesis value
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
