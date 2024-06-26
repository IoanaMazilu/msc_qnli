# The hypothesis talks about the same situation as the premise, but with different conditions
if T == 2/9 * (K-32) and T == 20:
    # The hypothesis condition is entailed by the premise
    label = "entailment"
elif T > 2/9 * (K-32) and T == 20:
    # The hypothesis condition contradicts the premise
    label = "contradiction"
else:
    # The hypothesis conditions are not met in the premise
    label = "neutral"

print(label)
