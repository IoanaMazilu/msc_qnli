# Premise: The spotted-eagle ray weighed about 75 to 80 pounds and had a 6-foot wingspan, Pino said.
# Hypothesis: Spotted eagle ray weighed 75 to 80 pounds, official says.
# Golden Label: entailment

weight_lower_limit_premise = 75
weight_upper_limit_premise = 80
weight_lower_limit_hypothesis = 75
weight_upper_limit_hypothesis = 80

# the hypothesis mentions the weight of the spotted-eagle ray, which is also mentioned in the premise
if weight_lower_limit_hypothesis < weight_lower_limit_premise or weight_upper_limit_hypothesis > weight_upper_limit_premise:
    # check if the weight range in the hypothesis contradicts the weight range mentioned in the premise
    label = "contradiction"
else:
    # if the weight range in the hypothesis does not contradict the weight range from the premise, we can infer entailment
    label = "entailment"

print(label)

