# Premise: A “ Sophie Germain ” prime is any positive prime number p for which 2 p + 1 is also prime.
# Hypothesis: A “ Sophie Germain ” prime is any positive prime number p for which less than 4 p + 1 is also prime.
# Golden Label: entailment

# define a variable for the constant multiplier of prime number p in both premise and hypothesis
multiplier_premise = 2
multiplier_hypothesis = 4

# the hypothesis refers to the definition of a "Sophie Germain" prime, also mentioned in the premise
if multiplier_hypothesis <= multiplier_premise:
    # check if the multiplier in the hypothesis contradicts the multiplier in the premise
    label = "contradiction"
else:
    # the hypothesis gives a broader condition for a prime number to be a "Sophie Germain" prime
    # any multiplier greater than 'multiplier_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

