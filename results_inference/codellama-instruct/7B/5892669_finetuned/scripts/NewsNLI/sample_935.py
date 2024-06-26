fatalities_premise = 4
infant_deaths_hypothesis = 5

# the hypothesis mentions the number of infant deaths linked to recliners, which is also referenced in the premise
# however, the number of fatalities in the premise is more than the number of infant deaths in the hypothesis
if fatalities_premise < infant_deaths_hypothesis:
    # check if the number of fatalities in the premise contradicts the number of infant deaths in the hypothesis
    label = "contradiction"
else:
    # if the number of fatalities in the premise does not contradict the number of infant deaths in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
