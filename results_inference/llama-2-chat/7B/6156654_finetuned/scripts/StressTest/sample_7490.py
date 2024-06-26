apples_anita_premise = 360
apples_anita_hypothesis = 560

# the hypothesis refers to Anita's apple count, which is also mentioned in the premise
if apples_anita_hypothesis!= apples_anita_premise:
    # check if the apple count in the hypothesis contradicts the apple count in the premise
    label = "contradiction"
else:
    # if the apple count in the hypothesis does not contradict the apple count in the premise, we can infer entailment
    label = "entailment"

print(label)
