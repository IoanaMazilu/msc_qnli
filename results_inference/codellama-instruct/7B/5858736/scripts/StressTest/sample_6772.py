# Define variables for the numerical entities in the premise and hypothesis
city_A_speed_premise = 50
city_B_speed_premise = 60
city_B_speed_hypothesis = 60
city_C_speed_hypothesis = 40

# Extract all quantities as valid numbers
city_A_speed_premise = int(city_A_speed_premise)
city_B_speed_premise = int(city_B_speed_premise)
city_B_speed_hypothesis = int(city_B_speed_hypothesis)
city_C_speed_hypothesis = int(city_C_speed_hypothesis)

# Check if the hypothesis values contradict the premise
if city_A_speed_hypothesis > city_A_speed_premise:
    label = "contradiction"
elif city_B_speed_hypothesis > city_B_speed_premise:
    label = "contradiction"
elif city_C_speed_hypothesis < city_C_speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
