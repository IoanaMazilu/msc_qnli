premise_greens_fee = 110
hypothesis_greens_fee = 110

# the hypothesis mentions the greens fee for the St. Andrews New Course, which is also mentioned in the premise
if hypothesis_greens_fee!= premise_greens_fee:
    # check if the greens fee in the hypothesis contradicts the greens fee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
