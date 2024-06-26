money_needed_premise = 363
money_needed_hypothesis = 215

# the hypothesis and premise mention the amount of money that Fannie and Freddie may need
if money_needed_premise < money_needed_hypothesis:
    # check if the amount of money in the hypothesis contradicts the premise
    label = "contradiction"
elif money_needed_premise > money_needed_hypothesis:
    # check if the amount of money in the hypothesis is less than the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
