# Premise: A “ Sophie Germain ” prime is any positive prime number p for which less than 4 p + 1 is also prime.
# Hypothesis: A “ Sophie Germain ” prime is any positive prime number p for which 2 p + 1 is also prime.
# Golden Label: neutral

premise_condition = 4
hypothesis_condition = 2

# the hypothesis refers to the condition for a number to be a 'Sophie Germain' prime, also mentioned in the premise
if premise_condition != hypothesis_condition:
    # check if the condition in the hypothesis contradicts the condition stated in the premise
    label = "contradiction"
else:
    # if the conditions are the same, the hypothesis is entailed from the premise
    label = "entailment"

print(label)

