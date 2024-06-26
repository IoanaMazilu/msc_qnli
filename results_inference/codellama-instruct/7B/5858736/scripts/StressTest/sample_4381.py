# Define variables with representative names for the numerical entities in both inputs
total_time_premise = 0
total_time_hypothesis = 0
speed_premise = 0
speed_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
total_time_premise = float(input("Enter the total time spent driving from City A to City B: "))
speed_premise = float(input("Enter the speed at which Andrew drove from City A to City B: "))
total_time_hypothesis = float(input("Enter the total time spent driving from City A to City B: "))
speed_hypothesis = float(input("Enter the speed at which Andrew drove from City A to City B: "))

# Use brief comments to explain what comparison you do between the defined variables
if total_time_premise <= total_time_hypothesis:
    # Check if the estimate of 'total_time_hypothesis' contradicts the total time spent driving in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # Check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
