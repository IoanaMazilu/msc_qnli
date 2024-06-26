# Define variables for the numerical entities in the premise and hypothesis
lenses_premise = 2
tubes_premise = 1
eyepieces_premise = 1
lenses_hypothesis = 7
tubes_hypothesis = 1
eyepieces_hypothesis = 1

# Check if the hypothesis values contradict the premise
if lenses_hypothesis > lenses_premise:
    label = "contradiction"
elif tubes_hypothesis!= tubes_premise:
    label = "contradiction"
elif eyepieces_hypothesis!= eyepieces_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
