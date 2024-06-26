wind_speed_premise = 75
wind_speed_hypothesis = 75
power_lines_downed_premise = 2000
power_lines_downed_hypothesis = 2000

# the hypothesis mentions the wind speed and the number of power lines downed, which are also mentioned in the premise
if wind_speed_hypothesis != wind_speed_premise:
    # check if the wind speed in the hypothesis contradicts the wind speed reported in the premise
    label = "contradiction"
elif power_lines_downed_hypothesis != power_lines_downed_premise:
    # check if the number of power lines downed from the hypothesis contradicts the number of power lines downed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
