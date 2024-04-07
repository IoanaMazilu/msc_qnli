# Premise: From a group of more than 1 boys & 4 girls a Committee of 4 persons is to be formed.
# Hypothesis: From a group of 6 boys & 4 girls a Committee of 4 persons is to be formed.
# Golden Label: neutral

boys_premise = 1
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# The hypothesis refers to the number of boys and girls and the committee size mentioned in the premise
if boys_hypothesis <= boys_premise:
    # Check if the number of boys in the hypothesis contradicts the estimate of more than 'boys_premise'
    label = "contradiction"
elif girls_premise != girls_hypothesis:
    # Check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_premise != committee_hypothesis:
    # Check if the committee size in the hypothesis contradicts the committee size reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of boys
    # Any number of boys greater than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

