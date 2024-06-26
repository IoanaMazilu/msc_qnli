chairs_premise = 3
chairs_hypothesis = 3

# the hypothesis talks about the number of chairs used to seat Susan, Daisy, and Tim, also referenced in the premise
if chairs_hypothesis < chairs_premise:
    # check if the hypothesis value contradicts the exact number of 'chairs_premise'
    label = "contradiction"
elif chairs_hypothesis == chairs_premise:
    # if the number of chairs in the hypothesis is equal to the number of chairs in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact number for the chairs
    # any number of chairs greater than 'chairs_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
