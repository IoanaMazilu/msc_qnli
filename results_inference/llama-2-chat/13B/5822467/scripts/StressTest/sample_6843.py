sacha_speed_premise = 7
bruno_speed_premise = 5
sacha_speed_hypothesis = float(input("Enter Sacha's speed (in meters per second): "))
bruno_speed_hypothesis = float(input("Enter Bruno's speed (in meters per second): "))

# Check if Sacha's speed contradicts the premise
if sacha_speed_hypothesis < sacha_speed_premise:
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    label = "contradiction"
else:
    # If both hypotheses are consistent with the premise, we can infer neutrality
    label = "neutral"

print(label)
