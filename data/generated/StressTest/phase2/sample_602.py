# Premise: If Yolanda's walking rate was 3 miles per hour and Bob т's was 4 miles per hour, how many miles had Bob walked when they met?
# Hypothesis: If Yolanda's walking rate was 6 miles per hour and Bob т's was 4 miles per hour, how many miles had Bob walked when they met?
# Golden Label: contradiction

yolanda_rate_premise = 3
bob_rate_premise = 4
yolanda_rate_hypothesis = 6
bob_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Yolanda and Bob, mentioned also in the premise
if yolanda_rate_premise != yolanda_rate_hypothesis:
    # check if Yolanda's walking rate in the hypothesis contradicts the premise
    label = "contradiction"
elif bob_rate_premise != bob_rate_hypothesis:
    # check if Bob's walking rate in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the walking rates in the premise and the hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)

