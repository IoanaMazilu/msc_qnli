# define variables with representative names for the numerical entities in both inputs
hour_premise = 1 + 3 * 60  # 1 hour at 50 mph + 3 hours at 60 mph
hour_hypothesis = 3 * 60  # less than 8 hours at 50 mph + 3 hours at 60 mph

# extract all quantities as valid numbers (integers or floats)
mph_premise = 50
mph_hypothesis = 60

# perform calculations if necessary
distance_premise = hour_premise * mph_premise  # 50 mph x 1 hour + 50 mph x 3 hours = 50 + 150 = 200 miles
distance_hypothesis = hour_hypothesis * mph_hypothesis  # 60 mph x 3 hours = 180 miles

# compare the variables
if distance_hypothesis < distance_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the premise and hypothesis are neutral
    label = "neutral"

print(label)
