# Premise: The product of all the possible units digits of Sophie Germain primes greater than 4 is.
# Hypothesis: The product of all the possible units digits of Sophie Germain primes greater than more than 1 is.
# Golden Label: entailment

units_digits_sophie_germain_primes_premise = 4
units_digits_sophie_germain_primes_hypothesis = 1

# the hypothesis refers to the possible units digits of Sophie Germain primes mentioned in the premise
if units_digits_sophie_germain_primes_hypothesis >= units_digits_sophie_germain_primes_premise:
    # check if the 'units_digits_sophie_germain_primes_hypothesis' contradicts the premise
    label = "contradiction"
elif units_digits_sophie_germain_primes_hypothesis < units_digits_sophie_germain_primes_premise:
    # check if the 'units_digits_sophie_germain_primes_hypothesis' is less than the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

