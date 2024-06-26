fuel_tank_premise = 40
fuel_tank_hypothesis = 60
cleveland_distance_premise = 480
cleveland_distance_hypothesis = 480

# the hypothesis refers to the fuel tank capacity and distance to Cleveland mentioned in the premise
if fuel_tank_premise != fuel_tank_hypothesis:
    # check if the fuel tank capacity in the hypothesis contradicts the fuel tank capacity in the premise
    label = "contradiction"
elif cleveland_distance_premise != cleveland_distance_hypothesis:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we have a neutral situation
    label = "neutral"

print(label)
