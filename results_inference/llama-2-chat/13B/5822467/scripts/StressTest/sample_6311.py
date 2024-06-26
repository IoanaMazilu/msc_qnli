boys_premise = 6
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = 1
girls_hypothesis = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in the committee
if boys_hypothesis + girls_hypothesis!= committee_size_hypothesis:
    # check if the number of boys and girls in the hypothesis contradicts the number of persons in the committee
    label = "contradiction"
elif boys_premise + girls_premise!= committee_size_premise:
    # check if the number of boys and girls in the premise contradicts the number of persons in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis and premise values for the number of boys and girls are consistent, we can infer neutrality
    label = "neutral"

print(label)
