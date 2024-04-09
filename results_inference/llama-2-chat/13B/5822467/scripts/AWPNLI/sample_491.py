peanuts_premise = 5.0
peanuts_given_premise = 2.0
peanuts_hypothesis = 1.0

# the hypothesis refers to the number of peanuts left, which is also mentioned in the premise
# compute the difference between the total peanuts in the premise and the number of peanuts given
remaining_peanuts_premise = peanuts_premise - peanuts_given_premise

if peanuts_hypothesis >= remaining_peanuts_premise:
    # check if the number of peanuts left in the hypothesis contradicts the estimate of more than'remaining_peanuts_premise'
    label = "contradiction"
elif peanuts_hypothesis!= peanuts_given_premise:
    # check if the number of peanuts given in the hypothesis contradicts the number of peanuts given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
