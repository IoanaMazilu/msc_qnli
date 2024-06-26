from_anwar_premise = 1600
from_anwar_hypothesis = 3600

# the hypothesis talks about the amount of money from Anwar, referenced also in the premise
if from_anwar_hypothesis <= from_anwar_premise:
    # check if the hypothesis value contradicts the estimate of more than 'from_anwar_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money from Anwar
    # any amount of money greater than 'from_anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
