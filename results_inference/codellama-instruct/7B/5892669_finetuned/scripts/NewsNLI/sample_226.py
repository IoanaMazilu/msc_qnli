japanese_descendants_premise = 1800000
japanese_descendants_hypothesis = 1800000

# the hypothesis mentions the number of Japanese descent people in Brazil, which is also referenced in the premise
if japanese_descendants_hypothesis!= japanese_descendants_premise:
    # check if the number of Japanese descent people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
