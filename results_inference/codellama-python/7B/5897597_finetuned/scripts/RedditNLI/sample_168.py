money_needed_premise = 363
money_needed_hypothesis = 215

# the hypothesis and premise mention the amount of money Fannie and Freddie may need
if money_needed_hypothesis!= money_needed_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
