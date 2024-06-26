apples_premise = 460
apples_hypothesis = 360

# the hypothesis refers to the number of apples possessed by Anita, mentioned in the premise
if apples_premise > apples_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'apples_premise'
    label = "contradiction"
elif apples_hypothesis!= apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
