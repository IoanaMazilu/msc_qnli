# Premise: From a group of more than 2 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: neutral

boys_premise = 2
girls_premise = 4
boys_hypothesis = 6
girls_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group, referenced also in the premise
if boys_hypothesis <= boys_premise or girls_hypothesis != girls_premise:
    # check if the hypothesis values contradict the estimates from the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

