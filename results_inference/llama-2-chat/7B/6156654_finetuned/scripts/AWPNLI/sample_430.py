oil_leaked_premise = 6522.0 - 5165.0
oil_leaked_hypothesis = 1357.0

# the hypothesis talks about the number of liters of oil leaked into the water, which is also mentioned in the premise
# however, the hypothesis provides a different number of liters than the premise
if oil_leaked_hypothesis!= oil_leaked_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
