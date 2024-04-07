# Premise: Jack had framed 24 photographs taken by Octavia, and 12 photographs taken by other photographers.
# Hypothesis: Jack had framed less than 84 photographs taken by Octavia, and 12 photographs taken by other photographers.
# Golden Label: entailment

photos_octavia_premise = 24
photos_octavia_hypothesis = 84
photos_others_premise = 12
photos_others_hypothesis = 12

# the hypothesis refers to the number of framed photos taken by Octavia and others, mentioned in the premise
if photos_octavia_hypothesis < photos_octavia_premise:
    # check if the estimate of 'photos_octavia_hypothesis' contradicts the number of Octavia's photos framed in the premise
    label = "contradiction"
elif photos_others_hypothesis != photos_others_premise:
    # check if the number of other photographers' photos framed in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

