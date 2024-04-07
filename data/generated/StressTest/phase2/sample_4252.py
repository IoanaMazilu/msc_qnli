# Premise: Arun purchased less than 50 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 30 kg of wheat at the rate of Rs.
# Golden Label: neutral

wheat_purchased_premise = 50
wheat_purchased_hypothesis = 30

# the hypothesis talks about the weight of wheat purchased by Arun, which is also mentioned in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the hypothesis value contradicts the estimate of less than 'wheat_purchased_premise'
    label = "contradiction"
elif wheat_purchased_hypothesis < wheat_purchased_premise:
    # the premise indicates that Arun purchased less than 'wheat_purchased_premise' kg of wheat
    # any weight less than 'wheat_purchased_premise' kg is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

