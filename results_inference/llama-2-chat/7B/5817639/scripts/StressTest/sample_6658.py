# Define variables for the premise and hypothesis
premise_average_speed = float(input("Premise: Assuming that Karen drives at an average speed of less than 80 mph and Tom drives at an average speed of 45 mph, how many Q miles will Tom drive before Karen wins the bet?"))
hypothesis_average_speed = float(input("Hypothesis: Assuming that Karen drives at an average speed of 60 mph and Tom drives at an average speed of 45 mph, how many Q miles will Tom drive before Karen wins the bet?"))

# Calculate the difference in average speed between the premise and hypothesis
speed_difference = hypothesis_average_speed - premise_average_speed

# Check if the speed difference contradicts the premise
if speed_difference > 0:
    # If the speed difference is positive, it contradicts the premise
    label = "contradiction"
else:
    # If the speed difference is negative or zero, it is consistent with the premise
    label = "entailment"
else:
    # If the speed difference is zero, it is neutral
    label = "neutral"

print(label)
