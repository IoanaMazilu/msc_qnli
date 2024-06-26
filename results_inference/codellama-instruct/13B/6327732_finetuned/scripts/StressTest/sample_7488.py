apples_anita_premise = 360
apples_anita_hypothesis = 460

# the hypothesis refers to the number of apples mentioned in the premise
if apples_anita_premise < apples_anita_hypothesis:
    # check if the estimate of 'apples_anita_hypothesis' contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
