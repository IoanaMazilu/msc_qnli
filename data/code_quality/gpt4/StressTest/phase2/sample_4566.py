days_walked_premise = 3
days_walked_hypothesis = 6

# the hypothesis refers to the number of days Ramzi walked, which is also mentioned in the premise
if days_walked_premise >= days_walked_hypothesis:
    # check if the number of days walked in the premise contradicts the 'less than' estimate in the hypothesis
    label = "contradiction"
elif days_walked_premise < days_walked_hypothesis:
    # if the number of days walked in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if both the premise and hypothesis values are equal, we can infer neutrality
    label = "neutral"

print(label)
