home_to_beach_speed_premise = 80
home_to_beach_speed_hypothesis = 40
beach_to_home_speed_premise = 70

# define variables with representative names for the numerical entities in both inputs
home_to_beach_distance = None
beach_to_home_distance = None

# extract all quantities as valid numbers (integers or floats)
home_to_beach_distance = round(home_to_beach_speed_premise * 2, 2)  # calculate distance traveled at 80 km/h
beach_to_home_distance = round(beach_to_home_speed_premise * 2, 2)  # calculate distance traveled at 70 km/h

# compare the distances traveled
if home_to_beach_distance > beach_to_home_distance:
    # the hypothesis implies a longer distance traveled than the premise
    label = "contradiction"
elif home_to_beach_distance == beach_to_home_distance:
    # the hypothesis and premise have the same distance traveled
    label = "neutral"
else:
    # the hypothesis implies a shorter distance traveled than the premise
    label = "entailment"

print(label)
