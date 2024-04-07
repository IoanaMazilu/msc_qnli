# Premise: less than 65 people entered a theater before Sujit.
# Hypothesis: 15 people entered a theater before Sujit.
# Golden Label: neutral

people_premise = 65
people_hypothesis = 15

# the hypothesis talks about the number of people who entered a theater before Sujit, referenced also in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

