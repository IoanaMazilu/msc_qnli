birds_premise = float(14.0)
birds_hypothesis = float(35.0)

# compare the number of birds in the premise and hypothesis
if birds_hypothesis > birds_premise:
    # the hypothesis talks about a larger number of birds than the premise, so it contradicts
    label = "contradiction"
elif birds_hypothesis == birds_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is less than the premise value, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
