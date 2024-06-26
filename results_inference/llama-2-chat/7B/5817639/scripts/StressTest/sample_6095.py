product_premise = 0
product_hypothesis = 0

# the hypothesis talks about the product of units digits of Sophie Germain primes, referenced also in the premise
if product_hypothesis <= product_premise:
    # check if the hypothesis value contradicts the estimate of the product of units digits of Sophie Germain primes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of units digits of Sophie Germain primes
    # any product greater than 'product_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
