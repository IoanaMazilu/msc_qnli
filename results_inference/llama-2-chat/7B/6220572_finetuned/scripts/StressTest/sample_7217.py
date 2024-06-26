fuel_tank_premise = 60
fuel_tank_hypothesis = 10
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis talks about the fuel tank and distance to Cleveland, referenced also in the premise
if fuel_tank_hypothesis >= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fuel_tank_premise'
    label = "contradiction"
elif distance_to_cleveland_hypothesis!= distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank and the distance to Cleveland
    # any fuel tank and distance to Cleveland consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
