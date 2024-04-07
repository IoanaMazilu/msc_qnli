# Premise: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the less than 40 miles from Marathon to Athens at a constant speed.
# Golden Label: contradiction

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

