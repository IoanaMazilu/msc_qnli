apples_maddie_premise = 48
apples_maddie_hypothesis = 18
apples_given = 22

# the hypothesis refers to the number of apples Maddie has, which is also mentioned in the premise
if apples_maddie_premise <= apples_maddie_hypothesis:
    # check if the estimate of 'apples_maddie_hypothesis' contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
