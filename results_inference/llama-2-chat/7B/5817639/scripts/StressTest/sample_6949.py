ages_premise = float(input("Premise: "))
ages_hypothesis = float(input("Hypothesis: "))

# the hypothesis talks about the ratio of the ages of two people, referenced also in the premise
if ages_hypothesis <= ages_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
