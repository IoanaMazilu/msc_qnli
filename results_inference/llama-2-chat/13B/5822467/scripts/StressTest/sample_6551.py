west_town_speed = 4
east_town_speed = 1

birds_start_premise = 2
birds_start_hypothesis = 2

# define variables with representative names for the numerical entities in both inputs
west_town_bird_speed = 3
east_town_bird_speed = 1

# extract all quantities as valid numbers (integers or floats)
west_town_bird_speed = float(west_town_bird_speed)
east_town_bird_speed = float(east_town_bird_speed)

# perform calculations if necessary
distance = west_town_bird_speed * birds_start_premise + east_town_bird_speed * birds_start_hypothesis

# compare the variables to infer a label
if west_town_bird_speed <= east_town_bird_speed:
    # check if the estimate of 'east_town_bird_speed' contradicts the number of birds starting from West-Town
    label = "contradiction"
elif birds_start_hypothesis!= birds_start_premise:
    # check if the number of birds starting from East-Town contradicts the number of birds starting from West-Town
    label = "contradiction"
elif distance!= 0:
    # check if the distance between the two birds contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
