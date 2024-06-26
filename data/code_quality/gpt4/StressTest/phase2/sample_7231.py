wheat_purchase_premise = 40
wheat_purchase_hypothesis = 30

# the hypothesis refers to the quantity of wheat purchased by Arun, which is also mentioned in the premise
if wheat_purchase_hypothesis >= wheat_purchase_premise:
    # check if the quantity of wheat in the hypothesis contradicts the premise's estimate of less than 'wheat_purchase_premise'
    label = "contradiction"
elif wheat_purchase_hypothesis < wheat_purchase_premise:
    # any quantity of wheat less than 'wheat_purchase_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the quantity of wheat
    # any number of wheat quantity less than 'wheat_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
