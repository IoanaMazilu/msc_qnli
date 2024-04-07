# Premise: Jack had framed 24 photographs taken by Octavia, and 12 photographs taken by other photographers.
# Hypothesis: Jack had framed 74 photographs taken by Octavia, and 12 photographs taken by other photographers.
# Golden Label: contradiction

photos_octavia_premise = 24
photos_octavia_hypothesis = 74
photos_other_premise = 12
photos_other_hypothesis = 12

# the hypothesis refers to the number of photos taken by Octavia and other photographers mentioned in the premise
if photos_octavia_hypothesis != photos_octavia_premise:
    # check if the number of photos taken by Octavia in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif photos_other_hypothesis != photos_other_premise:
    # check if the number of photos taken by other photographers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

