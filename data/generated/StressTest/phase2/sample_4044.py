# Premise: Jane and Thomas are among the 9 people from which a committee of 4 people is to be selected.
# Hypothesis: Jane and Thomas are among the more than 8 people from which a committee of 4 people is to be selected.
# Golden Label: entailment

people_premise = 9
people_hypothesis = 8

# the hypothesis talks about a group of people including Jane and Thomas, referenced also in the premise
if people_premise < people_hypothesis:
    # check if the number of people in the premise contradicts the number of people in the hypothesis
    label = "contradiction"
elif people_premise > people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the numbers of people in the premise and the hypothesis do not contradict each other, we can infer entailment
    label = "entailment"

print(label)

