# Premise: 15 people entered a theater before Sujit.
# Hypothesis: more than 15 people entered a theater before Sujit.
# Golden Label: contradiction

people_theater_premise = 15
people_theater_hypothesis = 15

# the hypothesis talks about the number of people entering a theater before Sujit, referenced also in the premise
if people_theater_hypothesis > people_theater_premise:
    # check if the hypothesis value contradicts the number of 'people_theater_premise'
    label = "contradiction"
elif people_theater_hypothesis == people_theater_premise:
    # the hypothesis value matches the premise, so we can infer entailment
    label = "entailment"
else:
    # any number of people less than 'people_theater_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

