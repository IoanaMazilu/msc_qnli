mpg_premise = 32
mpg_hypothesis = 82

# the hypothesis refers to the miles per gallon of Dan's car, which is also mentioned in the premise
if mpg_hypothesis <= mpg_premise:
    # check if the estimate of'mpg_hypothesis' contradicts the miles per gallon in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
