# Define variables for the numerical entities in the premise and hypothesis
city_A_speed_premise = 40
city_B_speed_premise = 60
city_B_speed_hypothesis = 60

# Extract all quantities as valid numbers
city_A_speed_hypothesis = 50

# Check if the hypothesis values contradict the premise
if city_A_speed_hypothesis > city_A_speed_premise:
    label = "contradiction"
elif city_B_speed_hypothesis!= city_B_speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
