interest_rate_begin_premise = 5
interest_rate_end_premise = 5.25
interest_rate_begin_hypothesis = 5
interest_rate_end_hypothesis = 5.25

# the hypothesis talks about the start and end interest rates which are also mentioned in the premise
if interest_rate_begin_hypothesis != interest_rate_begin_premise:
    # check if the beginning interest rate in the hypothesis contradicts the beginning interest rate in the premise
    label = "contradiction"
elif interest_rate_end_hypothesis != interest_rate_end_premise:
    # check if the end interest rate in the hypothesis contradicts the end interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
