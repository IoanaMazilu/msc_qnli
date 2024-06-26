# Define variables with representative names for the numerical entities in both inputs
average_speed_premise = float(input("Enter the average speed of Murali from A to C in the premise: "))
ratio_premise = float(input("Enter the ratio of distances between A to B and B to C in the premise: "))

average_speed_hypothesis = float(input("Enter the average speed of Murali from A to C in the hypothesis: "))
ratio_hypothesis = float(input("Enter the ratio of distances between A to B and B to C in the hypothesis: "))

# Extract all quantities as valid numbers (integers or floats)
if ratio_premise > ratio_hypothesis:
    # Check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis > 4/3 and ratio_hypothesis <= ratio_premise:
    # Check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif average_speed_hypothesis > average_speed_premise:
    # Check if the hypothesis value contradicts the estimate of the average speed in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
