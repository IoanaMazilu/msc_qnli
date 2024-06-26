earnings_premise = 374e6
earnings_hypothesis = -374e6

# the hypothesis talks about the net earnings of General Dynamics, which is also mentioned in the premise
if earnings_hypothesis != earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the earnings in the hypothesis do not contradict the earnings in the premise, we can infer entailment
    label = "entailment"

print(label)
