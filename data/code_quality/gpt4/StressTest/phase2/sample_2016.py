# Define the fraction of passengers from each continent in the premise
north_america_premise = 1/4
europe_premise = 1/8
africa_premise = 1/12
asia_premise = 1/6
other_premise = 36

# Define the fraction of passengers from each continent in the hypothesis
north_america_hypothesis = 7/4
europe_hypothesis = 1/8
africa_hypothesis = 1/12
asia_hypothesis = 1/6
other_hypothesis = 36

# The hypothesis is making a comparison to the number of passengers from each continent on the ship 
if north_america_hypothesis <= north_america_premise and europe_hypothesis == europe_premise and africa_hypothesis == africa_premise and asia_hypothesis == asia_premise and other_hypothesis == other_premise:
    # check if the fractions of passengers from each continent in the hypothesis contradict the fractions in the premise
    label = "contradiction"
elif north_america_hypothesis > north_america_premise and europe_hypothesis == europe_premise and africa_hypothesis == africa_premise and asia_hypothesis == asia_premise and other_hypothesis == other_premise:
    # check if the fractions of passengers from each continent in the hypothesis can be fully entailed from the premise
    label = "entailment"
else:
    # if the fractions of passengers from each continent in the hypothesis are consistent with the premise, but cannot be fully and explicitly entailed from it
    label = "neutral"

print(label)
