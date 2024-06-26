boys_premise = 6
girls_premise = 4
boys_hypothesis = 1
girls_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group, referenced also in the premise
if boys_hypothesis!= boys_premise or girls_hypothesis!= girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys and girls
    # any number of boys or girls consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
