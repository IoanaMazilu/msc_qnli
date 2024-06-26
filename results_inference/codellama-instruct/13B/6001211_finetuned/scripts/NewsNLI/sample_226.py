japanese_descendants_premise = 1.8e6
japanese_descendants_hypothesis = 1.8e6

# the hypothesis mentions the total number of Japanese descendants in Brazil, which is also mentioned in the premise
if japanese_descendants_hypothesis!= japanese_descendants_premise:
    # check if the total number of Japanese descendants in the hypothesis contradicts the total number in the premise
    label = "contradiction"
else:
    # if the total number of Japanese descendants in the hypothesis does not contradict the total number in the premise, we can infer entailment
    label = "entailment"

print(label)
