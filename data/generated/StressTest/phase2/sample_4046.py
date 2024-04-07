# Premise: Jane and Thomas are among the 9 people from which a committee of 4 people is to be selected.
# Hypothesis: Jane and Thomas are among the 5 people from which a committee of 4 people is to be selected.
# Golden Label: contradiction

people_premise = 9
people_hypothesis = 5
committee_size = 4

# the hypothesis talks about the number of people from which a committee is selected, which is also referenced in the premise
if people_hypothesis > people_premise:
    # check if the number of people in the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
elif people_hypothesis < committee_size:
    # check if the number of people in the hypothesis is less than the committee size, which would be a contradiction
    label = "contradiction"
else:
    # the premise gives only a maximum number for the people
    # any number of people less than or equal to 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

