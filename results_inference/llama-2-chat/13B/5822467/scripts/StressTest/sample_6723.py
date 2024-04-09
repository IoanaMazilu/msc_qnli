anwar_premise = 3600
anwar_hypothesis = 1600
percentage_premise = 6

# the hypothesis talks about the amount of money from Anwar at a certain percentage
if anwar_hypothesis > anwar_premise:
    # check if the hypothesis value contradicts the estimate of 'anwar_premise'
    label = "contradiction"
elif anwar_hypothesis == anwar_premise:
    # the premise and hypothesis values are the same, so there is no contradiction
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, so we can entail the hypothesis from the premise
    label = "entailment"

print(label)
