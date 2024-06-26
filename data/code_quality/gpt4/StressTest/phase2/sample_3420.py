committee_size_premise = 3
committee_size_hypothesis = 1
total_people = 6

# the hypothesis refers to the same selection process mentioned in the premise
if committee_size_hypothesis >= committee_size_premise:
    # check if the 'committee_size_hypothesis' contradicts the premise's requirement of a 3-people committee
    label = "contradiction"
elif committee_size_hypothesis < total_people and committee_size_premise > total_people:
    # check if the number of people in the hypothesis is less than total people and number of people in premise is more than total people
    label = "contradiction"
else:
    # the premise and hypothesis are talking about the same committee selection process, and the number of people in the committee in the hypothesis does not contradict the premise
    label = "entailment"

print(label)
