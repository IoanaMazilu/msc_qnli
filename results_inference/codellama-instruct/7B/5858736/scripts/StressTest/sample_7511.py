# Define variables with representative names for the numerical entities in both inputs (one variable per entity, per sentence)
distance_city_a_city_b_premise = 1
speed_premise = 50
time_premise = 1

distance_city_a_city_b_hypothesis = 7
speed_hypothesis = 50
time_hypothesis = 3

# Extract all quantities as valid numbers (integers or floats)
distance_city_a_city_b_premise = float(distance_city_a_city_b_premise)
speed_premise = float(speed_premise)
time_premise = float(time_premise)

distance_city_a_city_b_hypothesis = float(distance_city_a_city_b_hypothesis)
speed_hypothesis = float(speed_hypothesis)
time_hypothesis = float(time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables (do not use their values in the comments)
if distance_city_a_city_b_premise <= distance_city_a_city_b_hypothesis:
    # Check if the estimate of 'distance_city_a_city_b_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis:
    # Check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif time_premise!= time_hypothesis:
    # Check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
