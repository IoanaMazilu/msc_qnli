# Premise: Jane and Thomas are among the less than 8 people from which a committee of 4 people is to be selected.
# Hypothesis: Jane and Thomas are among the 7 people from which a committee of 4 people is to be selected.
# Golden Label: neutral

people_premise = 8
people_hypothesis = 7

# the hypothesis talks about the number of people (including Jane and Thomas) from which a committee is selected
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

