distance_meters_premise = 500
distance_meters_hypothesis = 800
running_speed_km_hr_premise = 15
running_speed_km_hr_hypothesis = 15

# the hypothesis refers to the distance covered and the running speed mentioned in the premise
if distance_meters_hypothesis <= distance_meters_premise:
    # check if the estimate of 'distance_meters_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
elif running_speed_km_hr_hypothesis!= running_speed_km_hr_premise:
    # check if the running speed in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
