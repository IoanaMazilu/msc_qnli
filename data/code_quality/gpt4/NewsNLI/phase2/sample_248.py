wounded_civilians_premise = 13
wounded_civilians_hypothesis = 13

# the hypothesis mentions the number of Afghan civilians wounded, which is also referenced in the premise
if wounded_civilians_hypothesis != wounded_civilians_premise:
    # check if the number of wounded civilians in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)
