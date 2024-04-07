# Premise: In 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 5979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: contradiction

year_premise = 1979
year_hypothesis = 5979
passengers_premise = 37.3 * (1/3)
passengers_hypothesis = 37.3 * (1/3)

# the hypothesis refers to the year and the number of passengers mentioned in the premise
if year_premise != year_hypothesis:
    # check if the year in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
elif passengers_premise != passengers_hypothesis:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

