# Premise: Mr Sharad started a business investing 50000.
# Hypothesis: Mr Sharad started a business investing more than 10000.
# Golden Label: entailment

investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the amount of investment Mr Sharad made, mentioned also in the premise
if investment_premise <= investment_hypothesis:
    # check if the amount of 'investment_hypothesis' contradicts the amount of investment made by Mr Sharad in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

