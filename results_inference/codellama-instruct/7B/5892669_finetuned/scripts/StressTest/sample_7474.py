sophie_germain_prime_premise = 4
sophie_germain_prime_hypothesis = 2

# the hypothesis refers to the definition of a 'Sophie Germain' prime mentioned in the premise
if sophie_germain_prime_hypothesis >= sophie_germain_prime_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific condition for a 'Sophie Germain' prime
    # any condition less than'sophie_germain_prime_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
