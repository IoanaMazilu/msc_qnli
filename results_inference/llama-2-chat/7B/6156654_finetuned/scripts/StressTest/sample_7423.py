floor_premise = 61
floor_hypothesis = 51
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about Albert getting on an elevator at the 51st floor, which contradicts the premise's floor number
if floor_hypothesis >= floor_premise:
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
