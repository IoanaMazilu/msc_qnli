people_accused_premise = 1000
people_died_hypothesis = 2

# the hypothesis mentions the number of people who have died after drinking a hallucinogenic potion, which is not mentioned in the premise
# the premise mentions the number of people accused of being witches in Gambia, who have been locked up in secret detention centers and forced to drink the potion
# the hypothesis's number of people who have died is higher than the number of people accused of being witches in the premise
if people_died_hypothesis > people_accused_premise:
    # check if the number of people who have died according to the hypothesis contradicts the number of people accused of being witches in the premise
    label = "contradiction"
else:
    # if the number of people who have died does not contradict the number of people accused of being witches, we cannot infer entailment or contradiction, so the relation is neutral
    label = "neutral"

print(label)
