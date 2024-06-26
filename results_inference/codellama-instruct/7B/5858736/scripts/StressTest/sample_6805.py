# Define variables for the numerical entities in the premise and hypothesis
distance_premise = 81
time_premise = 1
start_point_premise = "X"
end_point_premise = "Y"
start_point_hypothesis = "Y"
end_point_hypothesis = "X"
distance_hypothesis = 31
time_hypothesis = 1

# Extract all quantities as valid numbers
distance_premise = float(distance_premise)
time_premise = float(time_premise)
distance_hypothesis = float(distance_hypothesis)
time_hypothesis = float(time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if distance_hypothesis <= distance_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # Check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif start_point_hypothesis!= start_point_premise or end_point_hypothesis!= end_point_premise:
    # Check if the starting and ending points in the hypothesis contradict the starting and ending points reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
