address_premise = "1111 W. Dayton St., Madison, WI 53703"
address_hypothesis = "1111 W. Dayton St., Madison, WI 53703"

# the hypothesis mentions the Madison Police Department's address, which is also mentioned in the premise
if address_hypothesis!= address_premise:
    # check if the address from the hypothesis contradicts the address in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
