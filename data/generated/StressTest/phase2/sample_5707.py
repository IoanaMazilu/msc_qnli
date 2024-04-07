# Premise: Tanya is less than 75% more efficient than Sakshi.
# Hypothesis: Tanya is 25% more efficient than Sakshi.
# Golden Label: neutral

efficiency_premise = 75
efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Tanya compared to Sakshi, referenced also in the premise
if efficiency_hypothesis > efficiency_premise:
    # check if the hypothesis value contradicts the premise of Tanya being less efficient than 'efficiency_premise'% more than Sakshi
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # if the efficiency in the hypothesis is less than that in the premise, we can infer entailment
    label = "entailment"
else:
    # if the efficiency in the hypothesis equals that in the premise, there is no entailment or contradiction
    label = "neutral"

print(label)

