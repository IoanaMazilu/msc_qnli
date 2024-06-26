death_toll_premise = 128
death_toll_hypothesis = 146

# the hypothesis mentions the death toll, which is also mentioned in the premise
# however, the death toll in the hypothesis is higher than the one in the premise
if death_toll_hypothesis > death_toll_premise:
    # check if the death toll in the hypothesis contradicts the death toll reported in the premise
    label = "contradiction"
else:
    # if the death toll in the hypothesis does not contradict the death toll in the premise, we can infer entailment
    label = "entailment"

print(label)
