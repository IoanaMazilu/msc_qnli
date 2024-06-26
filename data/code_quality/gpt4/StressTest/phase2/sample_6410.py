offer_percentage_premise = 20
offer_percentage_hypothesis = 80

# the hypothesis talks about the discount offer for shirts, referenced also in the premise
if offer_percentage_hypothesis != offer_percentage_premise:
    # check if the offer percentage in the hypothesis contradicts the offer percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
