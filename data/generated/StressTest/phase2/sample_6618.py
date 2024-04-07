# Premise: Jane and Thomas are among the 7 people from which a committee of 4 people is to be selected.
# Hypothesis: Jane and Thomas are among the less than 8 people from which a committee of 4 people is to be selected.
# Golden Label: entailment

people_premise = 7
people_hypothesis = 8

# the hypothesis talks about the number of people from which a committee is to be selected, referenced also in the premise
if people_premise >= people_hypothesis:
    # check if the number of people in the premise contradicts the estimate of less than 'people_hypothesis'
    label = "contradiction"
else:
    # if the number of people in premise does not contradict the estimate from the hypothesis, we can infer entailment
    label = "entailment"

print(label)

