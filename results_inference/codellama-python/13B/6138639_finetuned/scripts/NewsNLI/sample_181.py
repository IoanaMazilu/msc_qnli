us_pledge_premise = 90000000
us_pledge_hypothesis = 90000000

# the hypothesis mentions the pledge of $90 million in emergency economic assistance, which is also mentioned in the premise
if us_pledge_hypothesis!= us_pledge_premise:
    # check if the pledge amount in the hypothesis contradicts the pledge amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
