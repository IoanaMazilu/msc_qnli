# define variables for the premise and hypothesis
sophie_germain_premise = "A Sophie Germain prime is any positive prime number p for which less than 4 p + 1 is also prime."
sophie_germain_hypothesis = "A Sophie Germain prime is any positive prime number p for which 2 p + 1 is also prime."

# extract numbers from the premise and hypothesis
less_than_4_premise = re.findall(r'\b(less than) 4\b', sophie_germain_premise)
less_than_4_hypothesis = re.findall(r'\b(less than) 4\b', sophie_germain_hypothesis)

# compare the numbers in the premise and hypothesis
if len(less_than_4_premise) > 0:
    # if the premise mentions less than 4, and the hypothesis mentions 2, we have a contradiction
    label = "contradiction"
elif len(less_than_4_hypothesis) > 0:
    # if the hypothesis mentions less than 4, and the premise does not, we have entailment
    label = "entailment"
else:
    # if neither the premise nor the hypothesis mention less than 4, we have neutrality
    label = "neutral"

print(label)
