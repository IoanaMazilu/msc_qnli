# the hypothesis refers to the product of the units digits of Sophie Germain primes greater than 8
product_hypothesis = 8

# the premise refers to the product of the units digits of Sophie Germain primes greater than 8
product_premise = 8

if product_hypothesis!= product_premise:
    # check if the product in the hypothesis contradicts the product in the premise
    label = "contradiction"
else:
    # if the product in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
