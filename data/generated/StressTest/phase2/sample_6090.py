# Premise: A “ Sophie Germain ” prime is any positive prime number p for which 2 p + 1 is also prime.
# Hypothesis: A “ Sophie Germain ” prime is any positive prime number p for which less than 3 p + 1 is also prime.
# Golden Label: entailment

# No numerical quantities to extract, but there is a numerical relation in both premise and hypothesis

# In the premise, 2*p + 1 is said to be prime
# In the hypothesis, <3*p + 1 is said to be prime
# The two are not the same, but the hypothesis does not contradict the premise
# However, the premise does not fully and explicitly entail the hypothesis either

label = "neutral"

print(label)

