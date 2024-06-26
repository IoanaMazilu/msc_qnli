premise_distance = 4.0
premise_speed = 3.0
hypothesis_time = 2.9

# define variables with representative names for the numerical entities in both inputs
distance_premise = premise_distance
speed_premise = premise_speed
time_hypothesis = hypothesis_time

# extract all quantities as valid numbers (integers or floats)
distance_hypothesis = float(time_hypothesis * speed_premise)

# compare the variables
if distance_hypothesis > distance_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif distance_hypothesis < distance_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
