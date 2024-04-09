# Define variables for the premise and hypothesis
baked_cookies_premise = 41.0
ate_cookies_premise = 38.0

# Define variable for the hypothesis
left_cookies_hypothesis = 0.0

# Compare the number of cookies baked and ate in the premise
if baked_cookies_premise + ate_cookies_premise == left_cookies_hypothesis:
    # If the total number of cookies baked and ate in the premise equals the number of cookies left in the hypothesis, we can infer entailment
    label = "entailment"
elif abs(left_cookies_hypothesis - (baked_cookies_premise + ate_cookies_premise)) < 0.000001:
    # If the difference between the number of cookies left in the hypothesis and the total number of cookies baked and ate in the premise is smaller than 0.000001, we can infer entailment
    label = "entailment"
else:
    # If the number of cookies left in the hypothesis contradicts the total number of cookies baked and ate in the premise, we can infer contradiction
    label = "contradiction"

print(label)
