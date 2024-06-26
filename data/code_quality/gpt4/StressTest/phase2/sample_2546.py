earnings_rise_premise = 20
earnings_rise_hypothesis = 20
earnings_premise = 560
earnings_hypothesis = 560

# the hypothesis talks about Albert's earnings rise and the earnings, also mentioned in the premise
if earnings_rise_hypothesis <= earnings_rise_premise:
    # check if the earnings rise percentage in the hypothesis contradicts the earnings rise percentage in the premise
    label = "contradiction"
elif earnings_hypothesis != earnings_premise:
    # check if the earnings in the hypothesis contradict the earnings in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings rise percentage
    # an earnings rise percentage equal to 'earnings_rise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
