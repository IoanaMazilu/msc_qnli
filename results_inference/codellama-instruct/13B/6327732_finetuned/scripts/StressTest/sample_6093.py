premise = "The product of all the possible units digits of Sophie Germain primes greater than 9 is."
hypothesis = "The product of all the possible units digits of Sophie Germain primes greater than more than 8 is."

# extract the numerical entities from the premise and hypothesis
premise_num = premise.split(" ")[-1]
hypothesis_num = hypothesis.split(" ")[-1]

# compare the numerical entities
if premise_num > hypothesis_num:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise value
    label = "entailment"

print(label)
