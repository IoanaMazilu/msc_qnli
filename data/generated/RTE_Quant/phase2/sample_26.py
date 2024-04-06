# Premise: With a diameter of 1,430 miles, Pluto is less than half the size of any other planet and only two-thirds as big as Earth's moon.
# Hypothesis: The terrestrial moon has a diameter of 3,746 kilometers.
# Golden Label: neutral

pluto_diameter_miles_premise = 1430
earth_moon_diameter_km_hypothesis = 3746

# convert the diameter of Pluto from miles to kilometers
# 1 mile is approximately 1.60934 kilometers
pluto_diameter_km_premise = pluto_diameter_miles_premise * 1.60934

# the premise states that the diameter of Pluto is less than two-thirds of the diameter of Earth's moon
# therefore, the diameter of Earth's moon should be greater than the diameter of Pluto divided by two-thirds
expected_earth_moon_diameter_km_premise = pluto_diameter_km_premise / (2/3)

# we can't infer entailment, as the premise doesn't offer a precise size for the moon
# we check for contradiction by comparing the Earth's moon diameter from the hypothesis with the expected diameter from the premise
if earth_moon_diameter_km_hypothesis != expected_earth_moon_diameter_km_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)

