premise_sum = 288
hypothesis_sum = 888
premise_discount = Rs.
hypothesis_discount = Rs.

# the hypothesis refers to the sum and discount mentioned in the premise
if hypothesis_sum <= premise_sum:
    # check if the estimate of 'hypothesis_sum' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif hypothesis_discount!= premise_discount:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
