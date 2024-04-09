anwar_premise = 1600
anwar_hypothesis = 3600
percentage_premise = 6

# the hypothesis talks about the amount of money from Anwar at a given percentage
if anwar_hypothesis <= (anwar_premise * percentage_premise / 100):
    # check if the hypothesis value contradicts the estimate of more than 'anwar_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money from Anwar
    # any amount of money greater than 'anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
