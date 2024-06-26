# the premise and hypothesis are similar
# the hypothesis adds a new condition to the premise

# the hypothesis conditions the value of T in the premise
if T >= 5/9 * (K-32):
    # check if the hypothesis condition is entailed by the premise
    label = "entailment"
elif T == 105:
    # check if the hypothesis condition contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis conditions the value of T in the premise, and T is not in the premise
    # then the hypothesis is neutral
    label = "neutral"

print(label)
