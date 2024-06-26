offer_premise = 40
offer_hypothesis = 10

# the hypothesis talks about the offer on shirts, which is referenced also in the premise
if offer_hypothesis != offer_premise:
    # check if the offer percentage in the hypothesis contradicts the offer percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
