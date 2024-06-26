interest_premise = 80920
interest_hypothesis = 10920

# the hypothesis refers to the amount of interest Mr Vishwas got, which is also mentioned in the premise
if interest_hypothesis >= interest_premise:
    # check if the hypothesis value contradicts the estimate of less than 'interest_premise'
    label = "contradiction"
else:
    # any interest amount less than 'interest_premise' is consistent with the premise, so we can infer entailment
    label = "entailment"

print(label)
