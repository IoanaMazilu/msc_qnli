anwar_premise = 1600
anwar_hypothesis = 3600

# the hypothesis refers to the number of shares sold by Anwar, mentioned in the premise
if anwar_hypothesis <= anwar_premise:
    # check if the estimate of 'anwar_hypothesis' contradicts the number of shares sold by Anwar in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares sold by Anwar
    # any number of shares greater than 'anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
