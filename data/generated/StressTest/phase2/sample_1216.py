# Premise: A “ Sophie Germain ” prime is any positive prime number p for which less than 5 p + 1 is also prime.
# Hypothesis: A “ Sophie Germain ” prime is any positive prime number p for which 2 p + 1 is also prime.
# Golden Label: neutral

premise_factor = 5
hypothesis_factor = 2

# both premise and hypothesis talk about the factor used in the definition of a "Sophie Germain" prime
if premise_factor != hypothesis_factor:
    # check if the factor in the hypothesis contradicts the factor mentioned in the premise
    label = "contradiction"
else:
    # if the factors are the same, the definitions in the premise and hypothesis are the same
    label = "entailment"

print(label)

