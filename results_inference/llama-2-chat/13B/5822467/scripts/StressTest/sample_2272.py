# Define variables with representative names for the numerical entities in both inputs
average_speed_premise = 0
average_speed_hypothesis = 0
distance_ratio_premise = 0
distance_ratio_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
average_speed_premise = float(input("What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 4:3? "))
average_speed_hypothesis = float(input("What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3?"))
distance_ratio_premise = float(input("What is the ratio of distances between A to B and B to C? "))
distance_ratio_hypothesis = float(input("What is the ratio of distances between A to B and B to C? "))

# Use brief comments to explain what comparison you do between the defined variables
# The hypothesis refers to the average speed of Murali from A to C and the ratio of distances between A to B and B to C

# Check if the hypothesis value contradicts the estimate of the ratio of distances between A to B and B to C in the premise
if distance_ratio_hypothesis!= distance_ratio_premise:
    # Check if the estimate of the ratio of distances between A to B and B to C contradicts the value of the ratio in the hypothesis
    label = "contradiction"

# Check if the average speed of Murali from A to C in the hypothesis is consistent with the estimate of the ratio of distances between A to B and B to C in the premise
elif distance_ratio_hypothesis == distance_ratio_premise:
    # Check if the estimate of the average speed of Murali from A to C in the hypothesis is consistent with the estimate of the ratio of distances between A to B and B to C in the premise
    label = "neutral"

else:
    # The premise gives only an estimate for the ratio of distances between A to B and B to C
    # Any ratio of distances between A to B and B to C greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
