artwork_return_rate_premise_lower = 5
artwork_return_rate_premise_upper = 10
artwork_return_rate_hypothesis_lower = 5
artwork_return_rate_hypothesis_upper = 10

# the hypothesis talks about the return rate of stolen artworks, which is also mentioned in the premise
if artwork_return_rate_hypothesis_lower!= artwork_return_rate_premise_lower or artwork_return_rate_hypothesis_upper!= artwork_return_rate_premise_upper:
    # check if the return rate in the hypothesis contradicts the return rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
