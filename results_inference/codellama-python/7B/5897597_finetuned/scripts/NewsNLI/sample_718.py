funds_raised_premise = 350000
funds_raised_hypothesis = 350000

# the hypothesis mentions the funds raised by the Jordan Thomas Foundation, which is also mentioned in the premise
if funds_raised_hypothesis!= funds_raised_premise:
    # check if the funds raised in the hypothesis contradicts the funds raised reported in the premise
    label = "contradiction"
else:
    # if the funds raised in the hypothesis do not contradict the funds raised in the premise, we can infer entailment
    label = "entailment"

print(label)
