# Define variables for the premise and hypothesis
town_R = "R"
town_B = "B"
speed_premise = 60
speed_hypothesis = 50

# Calculate the distance traveled by Tom
distance_premise = speed_premise * (town_B - town_R)
distance_hypothesis = speed_hypothesis * (town_B - town_R)

# Check if the hypothesis value contradicts the premise
if distance_hypothesis > distance_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
