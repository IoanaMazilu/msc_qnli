# defining the ratios of passengers from different continents in the premise and hypothesis
north_america_ratio_premise = 1/12
north_america_ratio_hypothesis = 1/12
europe_ratio_premise = 1/4
europe_ratio_hypothesis = 1/4
africa_ratio_premise = 1/9
africa_ratio_hypothesis = 1/9
asia_ratio_premise = 1/6
asia_ratio_hypothesis = 1/6
other_continents_ratio_premise = 42/100
other_continents_ratio_hypothesis = 42/100

# comparing the ratios of passengers from different continents in the premise and hypothesis
if north_america_ratio_premise!= north_america_ratio_hypothesis:
    label = "contradiction"
elif europe_ratio_premise!= europe_ratio_hypothesis:
    label = "contradiction"
elif africa_ratio_premise!= africa_ratio_hypothesis:
    label = "contradiction"
elif asia_ratio_premise!= asia_ratio_hypothesis:
    label = "contradiction"
elif other_continents_ratio_premise!= other_continents_ratio_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
