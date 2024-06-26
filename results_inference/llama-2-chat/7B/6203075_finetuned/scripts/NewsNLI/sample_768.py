percentage_faster_premise = 40
percentage_faster_hypothesis = 40

# the hypothesis mentions the percentage faster cooking than traditional utensils, which is also mentioned in the premise
if percentage_faster_hypothesis!= percentage_faster_premise:
    # check if the percentage faster cooking in the hypothesis contradicts the percentage faster cooking in the premise
    label = "contradiction"
else:
    # if the percentage faster cooking in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
