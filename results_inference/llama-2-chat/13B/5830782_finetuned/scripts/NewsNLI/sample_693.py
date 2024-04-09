active_psychiatrists_premise = 50
active_psychiatrists_hypothesis = 50
population_premise = 30000000

# the hypothesis mentions the number of active psychiatrists in the country, which is also mentioned in the premise
# however, the hypothesis does not mention the population, which is present in the premise
if active_psychiatrists_hypothesis!= active_psychiatrists_premise:
    # check if the number of active psychiatrists in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of active psychiatrists in the hypothesis does not contradict the number in the premise, we can infer neutrality
    label = "neutral"

print(label)
