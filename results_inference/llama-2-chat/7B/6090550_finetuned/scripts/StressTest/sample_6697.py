amount_premise = 5000
amount_hypothesis = 2000

# the hypothesis mentions a specific amount, which is less than the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis amount contradicts the premise's estimate of less than 'amount_premise'
    label = "contradiction"
elif amount_hypothesis < amount_premise:
    # the premise gives only an estimate for the amount
    # any amount less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
