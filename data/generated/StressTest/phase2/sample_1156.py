# Premise: In less than 2979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 1979 approximately 1/3 of the 37.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: neutral

year_premise = 2979
year_hypothesis = 1979
passengers_total = 37.3
kennedy_passengers_ratio = 1/3

# the hypothesis mentions the same year as the premise
if year_hypothesis >= year_premise:
    # check if 'year_hypothesis' contradicts the premise of being before 'year_premise'
    label = "contradiction"
else:
    # the premise only indicates that the event happened before 'year_premise'
    # it does not provide any explicit information about 'year_hypothesis'
    label = "neutral"

print(label)

