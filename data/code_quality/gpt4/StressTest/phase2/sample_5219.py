debentures_bought_premise = 50000
debentures_bought_hypothesis = 50000

# the hypothesis talks about the worth of debentures bought by Jaclyn, referenced also in the premise
if debentures_bought_hypothesis < debentures_bought_premise:
    # check if the hypothesized worth of debentures bought contradicts the value in the premise
    label = "contradiction"
elif debentures_bought_hypothesis > debentures_bought_premise:
    # check if the hypothesized worth of debentures bought contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesized worth of debentures bought does not contradict the value in the premise, we can infer entailment
    label = "entailment"

print(label)
