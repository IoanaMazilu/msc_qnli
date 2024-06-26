diameter_premise = 2.1
kilometers_hypothesis = 3.746e6

# the hypothesis talks about the diameter of the moon in kilometers which is not referenced in the premise (the diameter is given in meters)
# the hypothesis cannot be entailed from the premise, since the diameter of the moon in kilometers is unknown.
label = "neutral"

print(label)
