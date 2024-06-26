fundraising_ratio_premise = 7.5
fundraising_ratio_hypothesis = 7.5

# the hypothesis mentions the fundraising ratio between Walker and Barrett, which is also mentioned in the premise
if fundraising_ratio_hypothesis != fundraising_ratio_premise:
    # check if the fundraising ratio in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the fundraising ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
