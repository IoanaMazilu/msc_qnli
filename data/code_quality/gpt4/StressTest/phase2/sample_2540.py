dosage_premise = 15
dosage_hypothesis = 25

# the hypothesis talks about the dosage of Dosaxin which is also mentioned in the premise
if dosage_hypothesis == dosage_premise:
    # check if the dosage in the hypothesis is the same as the dosage in the premise
    label = "entailment"
else:
    # if the dosage in the hypothesis is not the same as the dosage in the premise, we have a contradiction
    label = "contradiction"

print(label)
