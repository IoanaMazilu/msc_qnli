# ratio of ages for Nishi and Vinnee in premise and hypothesis
nishi_vinnee_ratio_premise = [6, 5]
nishi_vinnee_ratio_hypothesis = [2, 5]

# the hypothesis talks about the ratio of ages of two people, also mentioned in the premise
if nishi_vinnee_ratio_premise != nishi_vinnee_ratio_hypothesis:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the ratio of ages in the hypothesis does not contradict the ratio of ages in the premise, we can infer entailment
    label = "entailment"

print(label)
