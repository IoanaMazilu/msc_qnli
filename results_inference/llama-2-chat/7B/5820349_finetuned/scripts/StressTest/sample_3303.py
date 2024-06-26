mpg_premise = 32
mpg_hypothesis = 62

# the hypothesis refers to the miles per gallon of Dan's car mentioned in the premise
if mpg_premise >= mpg_hypothesis:
    # check if the estimate of'mpg_premise' contradicts the number of miles per gallon in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
