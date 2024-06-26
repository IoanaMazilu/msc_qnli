wheat_purchased_premise = 30
wheat_purchased_hypothesis = 40

# the hypothesis refers to the amount of wheat purchased by Arun, which is also mentioned in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # the premise clearly states that Arun purchased 30kg of wheat
    # so, if the hypothesis claims less than or equal amount of wheat purchased, it's a contradiction
    label = "contradiction"
elif wheat_purchased_hypothesis > wheat_purchased_premise:
    # if the hypothesis claims more wheat purchased than the premise, it's consistent but cannot be explicitly entailed
    label = "neutral"
else:
    # if none of the above conditions are met, it's an entailment
    label = "entailment"

print(label)
