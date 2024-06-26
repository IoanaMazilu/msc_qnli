offer_premise = 5000000
offer_hypothesis = 5000000

# the hypothesis mentions the amount offered to Trump, which is also mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the amount offered in the hypothesis contradicts the amount offered in the premise
    label = "contradiction"
else:
    # if the amount offered in the hypothesis does not contradict the amount offered in the premise, we can infer entailment
    label = "entailment"

print(label)
