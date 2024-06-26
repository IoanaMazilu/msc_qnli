active_psychiatrists_premise = 50
active_psychiatrists_hypothesis = 50
population_premise = 30000000

# the hypothesis mentions the number of active psychiatrists in the country, which is also referenced in the premise
# however, the hypothesis does not mention the population of the country, which is provided in the premise
if active_psychiatrists_hypothesis!= active_psychiatrists_premise:
    # check if the number of active psychiatrists in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
