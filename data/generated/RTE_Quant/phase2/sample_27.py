# Premise: With a diameter of 5,230 kilometers, Ganymede is the largest satellite in the solar system-bigger than Mercury and about three-fourths the size of Mars.
# Hypothesis: The terrestrial moon has a diameter of 3,746 kilometers.
# Golden Label: neutral

diameter_ganymede_premise = 5230
diameter_moon_hypothesis = 3746

# the hypothesis talks about the diameter of the moon, which is not referenced in the premise
# the diameter of the moon cannot be entailed from the premise, since the premise only talks about Ganymede
label = "neutral"

print(label)

