people_premise = 8
people_hypothesis = 1
committee_size = 3

# the hypothesis refers to a subset of people (Jane and Thomas) that are also mentioned in the premise
# and the selection of a committee of a certain size, also referenced in both sentences
if people_premise < people_hypothesis:
    # check whether the number of people in the premise is fewer than the minimum number of people in the hypothesis
    label = "contradiction"
elif people_premise < committee_size:
    # check whether the number of people in the premise is fewer than the committee size
    label = "contradiction"
elif people_hypothesis < committee_size:
    # check whether the number of people in the hypothesis is fewer than the committee size
    label = "contradiction"
else:
    # if the number of people in both the premise and the hypothesis is equal or greater than the committee size,
    # we can infer entailment as the committee can be formed in either case
    label = "entailment"

print(label)
