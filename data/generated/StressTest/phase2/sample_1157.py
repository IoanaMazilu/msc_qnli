# Premise: In 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In less than 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: contradiction

year_premise = 1979
year_hypothesis = 1979
passengers_premise = 37.3
passengers_hypothesis = 37.3

# the hypothesis mentions the year and the number of passengers, both also referenced in the premise
if year_hypothesis >= year_premise:
    # check if 'year_hypothesis' contradicts 'year_premise'
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

