distance_premise = 40
distance_hypothesis = 40

# the hypothesis talks about the distance a runner runs from Marathon to Athens, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the specified distance of 'distance_premise'
    label = "contradiction"
else:
    # the premise gives a specific distance for the run
    # any distance less than 'distance_premise' contradicts the premise
    label = "contradiction"

print(label)
