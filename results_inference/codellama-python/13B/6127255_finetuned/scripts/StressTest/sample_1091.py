#matthew_rate_premise = 3
#matthew_rate_hypothesis = 3
#johnny_rate_premise = 4
#johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
# if the walking rates in the hypothesis are the same as in the premise, we can infer entailment
# if the walking rates in the hypothesis contradict the premise, we can infer contradiction
# if the walking rates in the hypothesis do not contradict the premise, but cannot be fully and explicitly entailed from the premise, we can infer neutrality

#if matthew_rate_hypothesis <= matthew_rate_premise:
#    # check if the hypothesis value contradicts the estimate of more than'matthew_rate_premise'
#    label = "contradiction"
#elif johnny_rate_hypothesis!= johnny_rate_premise:
#    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny reported in the premise
#    label = "contradiction"
#else:
#    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
#    label = "entailment"

#print(label)
#