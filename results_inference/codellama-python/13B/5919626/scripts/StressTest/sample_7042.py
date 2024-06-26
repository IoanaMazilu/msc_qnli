man_height_premise = 1.5
man_height_hypothesis = 1.5

# the hypothesis talks about the height of a man, referenced also in the premise
if man_height_hypothesis!= man_height_premise:
    # check if the height of the man in the hypothesis contradicts the height of the man in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of the man
    # any height of the man greater than'man_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
