needed_funds_premise = 363
needed_funds_hypothesis = 215

# the hypothesis and premise mention the potential amount of funds Fannie and Freddie may need
if needed_funds_hypothesis > needed_funds_premise:
    # check if the potential amount of funds in the hypothesis contradicts the potential amount of funds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
