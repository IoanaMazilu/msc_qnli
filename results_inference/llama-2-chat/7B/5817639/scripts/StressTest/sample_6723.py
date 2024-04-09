anwar_premise = 3600
anwar_hypothesis = 1600

# the hypothesis talks about a higher amount of money from Anwar at 6% p., compared to the premise
if anwar_hypothesis <= anwar_premise:
    # check if the hypothesis value contradicts the estimate of less than 'anwar_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money,
    # any amount of money greater than 'anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
