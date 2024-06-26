premise = "Fed raises rates again, sees two more hikes in 2018."
hypothesis = "Fed hikes rates, signals two more for 2018."

# extract numerical entities and their values from the premise and hypothesis
rate_premise = float(premise.split()[1])
hikes_premise = int(premise.split()[2])
rate_hypothesis = float(hypothesis.split()[1])
hikes_hypothesis = int(hypothesis.split()[2])

# compare the numerical entities and their values
if rate_premise!= rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif hikes_premise!= hikes_hypothesis:
    # check if the number of hikes in the hypothesis contradicts the number of hikes in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of hikes and the same interest rate
    # so we can infer entailment
    label = "entailment"

print(label)
