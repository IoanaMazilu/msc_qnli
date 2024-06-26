# The hypothesis refers to the proportion of passengers from different continents, which is also mentioned in the premise

north_america_premise = 1/12
north_america_hypothesis = 4/12

europe_premise = 1/8
europe_hypothesis = 1/8

africa_premise = 1/3
africa_hypothesis = 1/3

asia_premise = 1/6
asia_hypothesis = 1/6

other_premise = 35
other_hypothesis = 35

# the hypothesis refers to the number of passengers from different continents, which is also mentioned in the premise
if north_america_hypothesis >= north_america_premise:
    label = "contradiction"
elif europe_hypothesis!= europe_premise or africa_hypothesis!= africa_premise or asia_hypothesis!= asia_premise:
    label = "contradiction"
elif other_hypothesis!= other_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
