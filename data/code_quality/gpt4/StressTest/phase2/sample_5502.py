chairs_premise = 7
chairs_hypothesis = 1

# the hypothesis talks about the number of chairs in the seating arrangement, referenced also in the premise
if chairs_premise <= chairs_hypothesis:
    # check if the number of chairs in the premise contradicts the number of chairs in the hypothesis
    label = "contradiction"
elif chairs_hypothesis < chairs_premise:
    # check if the number of chairs in the hypothesis is less than the number of chairs in the premise
    label = "neutral"
else:
    # if the number of chairs in the hypothesis is equal to the number of chairs in the premise, we can infer entailment
    label = "entailment"

print(label)
