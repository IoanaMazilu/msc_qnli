disqualified_women_premise = 4
disqualified_women_hypothesis = 4

# the hypothesis mentions the number of women disqualified for overdressing, which is also mentioned in the premise
if disqualified_women_hypothesis!= disqualified_women_premise:
    # check if the number of disqualified women in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of disqualified women in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
