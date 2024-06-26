# Define variables for the premise and hypothesis
units_digits_premise = 8
units_digits_hypothesis = 4

# Extract the product of all the possible units digits of Sophie Germain primes greater than 'units_digits_premise'
product_premise = 100

# Extract the product of all the possible units digits of Sophie Germain primes greater than 'units_digits_hypothesis'
product_hypothesis = 10

# Check if the product of the hypothesis contradicts the product of the premise
if product_hypothesis <= product_premise:
    # The hypothesis value contradicts the product of the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the product of the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
