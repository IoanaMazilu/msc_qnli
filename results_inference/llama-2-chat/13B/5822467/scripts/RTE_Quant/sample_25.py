# define variables with representative names for the numerical entities in both inputs
moon_cake_diameter_premise = 2.1
terrestrial_moon_diameter_hypothesis = 3746

# extract all quantities as valid numbers (integers or floats)
moon_cake_diameter_premise = float(moon_cake_diameter_premise)
terrestrial_moon_diameter_hypothesis = float(terrestrial_moon_diameter_hypothesis)

# compare the variables
if terrestrial_moon_diameter_hypothesis > moon_cake_diameter_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif terrestrial_moon_diameter_hypothesis < moon_cake_diameter_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
