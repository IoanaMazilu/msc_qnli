gloves_premise = 20
gloves_hypothesis = 40

# the hypothesis talks about the number of gloves Andy has, referenced also in the premise
if gloves_hypothesis <= gloves_premise:
    # check if the hypothesis value contradicts the number of 'gloves_premise'
    label = "contradiction"
elif gloves_hypothesis > gloves_premise:
    # check if the hypothesis value is more than the number of 'gloves_premise'
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise, we can infer entailment
    label = "entailment"

print(label)
