# Premise: Flare with Fin-X technology is the name of a new range of saucepans that claim to cook 40% faster than traditional pans, thus saving both time and energy.
# Hypothesis: Futuristic saucepans can cook food 40% faster than our traditional utensils.
# Golden Label: neutral

faster_cooking_premise = 0.4
faster_cooking_hypothesis = 0.4

# the hypothesis mentions the increased cooking speed of the saucepans, which is also mentioned in the premise
if faster_cooking_hypothesis != faster_cooking_premise:
    # check if the cooking speed in the hypothesis contradicts the cooking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

