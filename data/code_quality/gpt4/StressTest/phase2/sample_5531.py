debt_premise = 60000
debt_hypothesis = 60000

# the hypothesis talks about the amount of debentures bought by Jaclyn, referenced also in the premise
if debt_hypothesis < debt_premise:
    # check if the hypothesis value contradicts the 'debt_premise'
    label = "contradiction"
elif debt_hypothesis == debt_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    label = "neutral"

print(label)
