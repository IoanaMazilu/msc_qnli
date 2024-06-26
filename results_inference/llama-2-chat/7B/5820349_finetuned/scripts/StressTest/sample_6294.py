money_given_premise = 40
money_given_hypothesis = 60

# the hypothesis refers to the percentage of money given to the wife, which is also mentioned in the premise
if money_given_premise >= money_given_hypothesis:
    # check if the percentage of money given in the premise contradicts the hypothesis
    label = "contradiction"
elif money_given_premise < money_given_hypothesis:
    # if the percentage of money given in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the premise and hypothesis values are equal, we can infer neutrality
    label = "neutral"

print(label)
