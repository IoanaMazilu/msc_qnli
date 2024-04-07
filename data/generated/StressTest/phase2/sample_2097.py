# Premise: In 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In less than 3979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: entailment

year_premise = 1979
year_hypothesis = 3979
passengers_premise = 37.3 * 1/3
passengers_hypothesis = 37.3 * 1/3

# the hypothesis refers to the same fraction of passengers at Kennedy Airport, but in a different year
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis year is less than the premise year and the number of passengers is the same, we can infer entailment
    label = "entailment"

print(label)

