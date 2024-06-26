committee_size_premise = 4
committee_size_hypothesis = 4
total_people = 7

# the hypothesis refers to the size of the committee selection mentioned in the premise
if committee_size_hypothesis > committee_size_premise:
    # check if the committee size in the hypothesis contradicts the committee size in the premise
    label = "contradiction"
elif total_people < committee_size_hypothesis:
    # check if the total people are less than the committee size in the hypothesis
    label = "contradiction"
else:
    # if the committee size in the hypothesis does not contradict the premise, we cannot fully and explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)
