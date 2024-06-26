peanuts_premise = 4
peanuts_hypothesis = 7
additional_peanuts_premise = 8
additional_peanuts_hypothesis = 8

# the hypothesis refers to the number of peanuts in a box and the number of additional peanuts in the premise
if peanuts_hypothesis == peanuts_premise + additional_peanuts_premise:
    # check if the number of peanuts in the hypothesis contradicts the estimate of 'peanuts_premise + additional_peanuts_premise'
    label = "contradiction"
elif additional_peanuts_hypothesis!= additional_peanuts_premise:
    # check if the number of additional peanuts in the hypothesis contradicts the number of additional peanuts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
