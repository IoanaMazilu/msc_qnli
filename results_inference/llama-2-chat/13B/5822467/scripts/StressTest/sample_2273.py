# Define variables for the numerical entities in the premise and hypothesis
average_speed_premise = float(input("Enter the average speed of Murali from A to C given the ratio of distances is 2:3: "))
average_speed_hypothesis = float(input("Enter the average speed of Murali from A to C given the ratio of distances is 8:3: "))
distance_ratio_premise = 2 / 3
distance_ratio_hypothesis = 8 / 3

# Check if the hypothesis value contradicts the premise value
if average_speed_hypothesis < average_speed_premise:
    label = "contradiction"
elif average_speed_hypothesis > average_speed_premise:
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise value, there is no contradiction or entailment
    label = "neutral"

print(label)
