fraction_premise = 7/12
fraction_hypothesis = 7/12

# The hypothesis talks about the fraction of the sum of money E that Anup was asked to find, which is also referenced in the premise
if fraction_hypothesis >= fraction_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the fraction in the hypothesis is less than the fraction in the premise, 
    # it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
