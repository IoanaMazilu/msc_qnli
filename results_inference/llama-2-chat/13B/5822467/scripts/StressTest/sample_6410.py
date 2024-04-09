discount_premise = 20
discount_hypothesis = 80
shirt_price_premise = Rs.
shirt_price_hypothesis = Rs.

# the hypothesis talks about the discount percentage and shirt price, referenced also in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
elif shirt_price_hypothesis!= shirt_price_premise:
    # check if the shirt price in the hypothesis contradicts the shirt price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
