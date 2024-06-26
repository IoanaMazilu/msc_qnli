sophie_germain_units_premise = 9
sophie_germain_units_hypothesis = 8

# both premise and hypothesis refer to the product of the units digits of Sophie Germain primes
if sophie_germain_units_hypothesis != sophie_germain_units_premise:
    # check if the hypothesis value contradicts the premise one
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we infer entailment
    label = "entailment"

print(label)
