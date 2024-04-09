maddie_apples_premise = 88
maddie_apples_hypothesis = 18
mike_apples_premise = 12

# the hypothesis refers to the number of apples Maddie has after giving some to Mike
if maddie_apples_premise <= maddie_apples_hypothesis:
    # check if the estimate of'maddie_apples_hypothesis' contradicts the number of apples Maddie has reported in the premise
    label = "contradiction"
elif maddie_apples_hypothesis - mike_apples_premise > 0:
    # check if the number of apples Maddie has after giving some to Mike contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
