loss_premise = 0
loss_hypothesis = 6
interest_rate = 4
years_premise = 2
years_hypothesis = 6

# the hypothesis refers to the number of years and the interest rate mentioned in the premise
if years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate!= 4 or loss_premise == 0:
    # check if the interest rate or the initial loss in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
