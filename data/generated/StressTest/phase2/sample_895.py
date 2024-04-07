# Premise: Arun purchased less than 60 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 30 kg of wheat at the rate of Rs.
# Golden Label: neutral

wheat_purchased_premise = 60
wheat_purchased_hypothesis = 30

# the hypothesis refers to the quantity of wheat purchased, which is also mentioned in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the quantity of wheat purchased in the hypothesis contradicts the estimate of less than 'wheat_purchased_premise'
    label = "contradiction"
elif wheat_purchased_hypothesis > wheat_purchased_premise:
    # check if the quantity of wheat purchased in the hypothesis contradicts the estimate of less than 'wheat_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of wheat purchased
    # any quantity less than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

