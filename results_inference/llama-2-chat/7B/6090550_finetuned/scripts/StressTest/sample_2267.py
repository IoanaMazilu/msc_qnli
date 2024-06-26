gloves_premise = 20
gloves_hypothesis = 20

# the hypothesis talks about the number of gloves Andy has, which is also mentioned in the premise
if gloves_hypothesis!= gloves_premise:
    # check if the number of gloves in the hypothesis contradicts the number of gloves in the premise
    label = "contradiction"
else:
    # if the number of gloves in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
