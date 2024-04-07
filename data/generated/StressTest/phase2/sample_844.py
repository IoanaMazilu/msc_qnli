# Premise: Adam sat with his friends in the Chinnaswamy stadium at Madurai to watch the less than 700 metres running race organized by the Asian athletics Association.
# Hypothesis: Adam sat with his friends in the Chinnaswamy stadium at Madurai to watch the 100 metres running race organized by the Asian athletics Association.
# Golden Label: neutral

race_length_premise = 700
race_length_hypothesis = 100

# the hypothesis refers to a specific race length that is also mentioned in the premise
if race_length_hypothesis >= race_length_premise:
    # check if the hypothesis value contradicts the premise statement of less than 'race_length_premise'
    label = "contradiction"
elif race_length_hypothesis < race_length_premise:
    # if the race length in the hypothesis is less than the one from the premise
    # it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

