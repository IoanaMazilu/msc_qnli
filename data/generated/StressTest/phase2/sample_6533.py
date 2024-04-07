# Premise: In 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 7979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: contradiction

year_premise = 1979
year_hypothesis = 7979
passengers_premise = 37.3
passengers_hypothesis = 37.3
fraction_premise = 1/3
fraction_hypothesis = 1/3

# the hypothesis refers to the same fraction of passengers and total passengers as in the premise
# but in a different year
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
elif fraction_hypothesis != fraction_premise or passengers_hypothesis != passengers_premise:
    # check if the fraction of passengers or total passengers in the hypothesis contradicts the ones mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

