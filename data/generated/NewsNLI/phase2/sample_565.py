# Premise: Only seven men in history have achieved the feat of winning all four of the grand slams:Wimbledon, and the United States, Australian and French Opens.
# Hypothesis: Only seven men have completed a career grand slam in singles.
# Golden Label: neutral

men_premise = 7
men_hypothesis = 7

# the hypothesis mentions the number of men who have completed a career grand slam, which is also mentioned in the premise
if men_hypothesis != men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the number of men in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

