cassini_height_premise = 7  # in meters
scientific_instruments_premise = 12
probe_instruments_premise = 6
saturn_moon_diameter_hypothesis = 5100  # in kilometers

# the hypothesis talks about the diameter of the moon Titan which is not referenced in the premise
# the hypothesis cannot be entailed from the premise, since the diameter of the moon Titan is unknown.
label = "neutral"

print(label)