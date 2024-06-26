neha_premise = 70
neha_hypothesis = 10
sonali_priyanka_premise = 15
sonali_priyanka_hypothesis = 15
sadaf_tanu_premise = 10
sadaf_tanu_hypothesis = 10

# the hypothesis refers to the same individuals as the premise
# so we compare their quantities according to the premise and hypothesis

if neha_premise < neha_hypothesis or sonali_priyanka_premise != sonali_priyanka_hypothesis or sadaf_tanu_premise != sadaf_tanu_hypothesis:
    # check if any of the hypothesis values contradict the premise's corresponding values
    label = "contradiction"
elif neha_premise == neha_hypothesis and sonali_priyanka_premise == sonali_priyanka_hypothesis and sadaf_tanu_premise == sadaf_tanu_hypothesis:
    # if all the hypothesis values are equal to the premise's corresponding values, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and are not exactly equal, we infer neutral
    label = "neutral"

print(label)
