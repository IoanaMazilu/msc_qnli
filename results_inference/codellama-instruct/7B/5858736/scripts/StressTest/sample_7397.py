# Define variables for the premise and hypothesis
town_R = "R"
town_B = "B"
speed_premise = 60
speed_hypothesis = 70

# Calculate the distance traveled by Tom in each case
distance_premise = speed_premise * (town_B - town_R)
distance_hypothesis = speed_hypothesis * (town_B - town_R)

# Check if the hypothesis contradicts the premise
if distance_hypothesis > distance_premise:
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
