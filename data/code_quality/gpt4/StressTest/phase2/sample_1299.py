from_anwar_premise = 4050
from_anwar_hypothesis = 3050

# the hypothesis refers to the quantity obtained from Anwar mentioned in the premise
if from_anwar_hypothesis >= from_anwar_premise:
    # check if the estimate of 'from_anwar_hypothesis' contradicts the number obtained from Anwar in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
