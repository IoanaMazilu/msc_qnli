earnings_premise = 19800
earnings_hypothesis = 19800

# the hypothesis talks about the earnings of Shridhar, which is also referenced in the premise
if earnings_hypothesis < earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
elif earnings_hypothesis == earnings_premise:
    # if the earnings in the hypothesis is equal to the earnings in the premise, it contradicts the 'more than' condition in the hypothesis
    label = "contradiction"
else:
    # the premise gives the exact earnings of Shridhar
    # any earnings higher than 'earnings_premise' is not explicitly stated in the premise
    label = "neutral"

print(label)
