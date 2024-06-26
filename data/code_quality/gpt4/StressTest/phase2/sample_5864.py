participants_premise = 6
participants_hypothesis = 6

# the hypothesis refers to the number of participants in a race, also mentioned in the premise
if participants_hypothesis < participants_premise:
    # check if the hypothesis value contradicts the number of participants reported in the premise
    label = "contradiction"
elif participants_hypothesis == participants_premise:
    # check if the number of participants in the hypothesis exactly matches the number in the premise
    label = "entailment"
else:
    # the hypothesis suggests there are more participants than stated in the premise
    label = "neutral"

print(label)
