peanuts_premise = 4
peanuts_hypothesis = 2

# the hypothesis refers to the number of peanuts in a box
if peanuts_hypothesis <= peanuts_premise:
    # check if the hypothesis value contradicts the estimate of 'peanuts_premise'
    label = "contradiction"
elif peanuts_premise + 12!= peanuts_hypothesis:
    # check if the number of peanuts in the hypothesis contradicts the number of peanuts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
