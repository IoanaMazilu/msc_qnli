# Premise: In a BCCI meeting there are less than 54 people.
# Hypothesis: In a BCCI meeting there are 14 people.
# Golden Label: neutral

people_premise = 54
people_hypothesis = 14

# the hypothesis refers to the number of people in a BCCI meeting, also mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the estimate of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

