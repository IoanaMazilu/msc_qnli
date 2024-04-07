# Premise: Arun purchased more than 10 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 30 kg of wheat at the rate of Rs.
# Golden Label: neutral

wheat_purchased_premise = 10
wheat_purchased_hypothesis = 30

# the hypothesis talks about the quantity of wheat purchased, referenced also in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'wheat_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of wheat purchased
    # any quantity of wheat greater than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

