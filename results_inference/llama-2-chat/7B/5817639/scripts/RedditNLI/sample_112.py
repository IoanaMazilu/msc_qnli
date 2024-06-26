percentage_premise = 14
percentage_hypothesis = 14

# check if the hypothesis and premise have the same percentage value
if percentage_hypothesis == percentage_premise:
    # if the values are the same, the hypothesis can be entailed from the premise
    label = "entailment"
elif percentage_hypothesis < percentage_premise:
    # if the value in the hypothesis is smaller than the value in the premise, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the values are different, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
