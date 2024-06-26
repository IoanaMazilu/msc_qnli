raised_funds_premise = 350000
raised_funds_hypothesis = 350000

# the hypothesis mentions the amount of funds raised by the Jordan Thomas Foundation, which is also mentioned in the premise
if raised_funds_hypothesis!= raised_funds_premise:
    # check if the amount of funds raised in the hypothesis contradicts the amount of funds raised reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
