earnings_premise = 320
earnings_hypothesis = 720

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_premise >= earnings_hypothesis:
    # check if the earnings in the hypothesis contradict the earnings reported in the premise
    label = "contradiction"
elif earnings_premise < earnings_hypothesis:
    # check if the earnings in the hypothesis entail the earnings reported in the premise
    label = "entailment"
else:
    # if the earnings values do not contradict or entail each other, the relation is neutral
    label = "neutral"

print(label)
