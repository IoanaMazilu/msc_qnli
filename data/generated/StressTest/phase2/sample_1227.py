# Premise: If 36 of the photographs in the exhibition were taken by Octavia, how many photographs were either framed by Jack or taken by Octavia?
# Hypothesis: If less than 86 of the photographs in the exhibition were taken by Octavia, how many photographs were either framed by Jack or taken by Octavia?
# Golden Label: entailment

photos_taken_by_octavia_premise = 36
photos_taken_by_octavia_hypothesis = 86

# the hypothesis refers to the number of photos taken by Octavia in the exhibition, mentioned in the premise
if photos_taken_by_octavia_hypothesis < photos_taken_by_octavia_premise:
    # check if the hypothesis value contradicts the number of photos taken by Octavia in the premise
    label = "contradiction"
elif photos_taken_by_octavia_hypothesis == photos_taken_by_octavia_premise:
    # check if the exact number of photos taken by Octavia in hypothesis is equal to the number in premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise ones, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

