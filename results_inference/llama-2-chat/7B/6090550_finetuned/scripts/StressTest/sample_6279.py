ratio_premise = 7/3/2
ratio_hypothesis = 8/3/2

# the hypothesis talks about the ratio of questions submitted by Rajat, Vikas and Abhishek
if ratio_premise >= ratio_hypothesis:
    # check if the ratio in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the ratio in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
