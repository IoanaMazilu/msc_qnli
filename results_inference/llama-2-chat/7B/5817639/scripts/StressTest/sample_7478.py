product_premise = 0
product_hypothesis = 0

# the hypothesis talks about the product of units digits of Sophie Germain primes greater than 4
if product_hypothesis <= product_premise:
    # check if the hypothesis value contradicts the estimate of the product of units digits in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the product of units digits, but the hypothesis provides a different value
    label = "neutral"

print(label)
