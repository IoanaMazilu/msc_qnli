premise_bobby = 38
premise_bonny = 56
premise_vijay = 66
premise_libin = 75

hypothesis_bobby = 88
hypothesis_bonny = 56
hypothesis_vijay = 66
hypothesis_libin = 75

# the hypothesis refers to the scores mentioned in the premise
if hypothesis_bobby > premise_bobby:
    # check if the estimate of 'hypothesis_bobby' contradicts the score of Bobby in the premise
    label = "contradiction"
elif hypothesis_libin!= premise_libin:
    # check if the score of Libin in the hypothesis contradicts the score of Libin reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
