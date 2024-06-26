participants_premise = 3
participants_hypothesis = 3

# the hypothesis talks about the number of participants in a race, which is also referenced in the premise
if participants_hypothesis < participants_premise:
    # check if the hypothesis value contradicts the exact number of 'participants_premise'
    label = "contradiction"
elif participants_hypothesis == participants_premise:
    # if the hypothesis value equals the premise one, we can infer entailment
    label = "entailment"
else:
    # any number of participants greater than 'participants_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
