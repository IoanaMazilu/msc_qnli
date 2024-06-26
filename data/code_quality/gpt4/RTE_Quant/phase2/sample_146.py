diameter_io_miles = 2236
diameter_io_kilometers = 3598
diameter_moon_kilometers_hypothesis = 3746

# the hypothesis talks about the diameter of the Earth's moon
# the premise only provides the information that Io is slightly larger than the Earth's moon, but does not provide an exact value for the diameter of the Earth's moon.
# Therefore, the hypothesis cannot be entailed from the premise.
# However, as the diameter of the Earth's moon provided in the hypothesis is larger than the diameter of Io (which is said to be slightly larger than the Earth's moon), this would be a contradiction.
if diameter_moon_kilometers_hypothesis <= diameter_io_kilometers:
    label = "contradiction"
else:
    label = "neutral"

print(label)
