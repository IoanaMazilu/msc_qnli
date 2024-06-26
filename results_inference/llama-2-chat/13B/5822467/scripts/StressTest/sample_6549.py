west_town_speed = 4
east_town_speed = 1

# define variables with representative names for the numerical entities in both inputs
bird_speed_premise = west_town_speed
bird_speed_hypothesis = east_town_speed

# extract all quantities as valid numbers (integers or floats)
bird_speed_premise = int(bird_speed_premise)
bird_speed_hypothesis = int(bird_speed_hypothesis)

# compare the variables
if bird_speed_hypothesis < bird_speed_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif bird_speed_hypothesis == bird_speed_premise:
    # the hypothesis is neutral with respect to the premise
    label = "neutral"
else:
    # the hypothesis entails the premise
    label = "entailment"

print(label)
