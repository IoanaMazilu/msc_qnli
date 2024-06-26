diameter_moon_premise = 25 # in miles
diameter_moon_hypothesis = 5100 # in kilometers

# convert miles to kilometers
diameter_moon_premise_km = diameter_moon_premise * 1.60934

# the hypothesis talks about the diameter of the moon Titan which is not the same moon mentioned in the premise
# the hypothesis cannot be entailed from the premise, since they refer to different moons.
label = "neutral"

print(label)
