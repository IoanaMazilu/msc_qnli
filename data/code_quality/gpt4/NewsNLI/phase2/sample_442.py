women_disqualified_premise = 4
women_disqualified_hypothesis = 4

# the hypothesis mentions the number of women disqualified for overdressing, which is also mentioned in the premise
if women_disqualified_hypothesis != women_disqualified_premise:
    # check if the number of women disqualified in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of women disqualified in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
