north_america_premise = 1/12
europe_premise = 1/4
africa_premise = 2/9
asia_premise = 1/6
other_continents_premise = 50

hypothesis_na = less_than(7/12, north_america_premise)
hypothesis_eu = less_than(1/4, europe_premise)
hypothesis_af = less_than(2/9, africa_premise)
hypothesis_as = less_than(1/6, asia_premise)
hypothesis_oc = less_than(50, other_continents_premise)

# check if the hypothesis values contradict the premise values
if hypothesis_na or hypothesis_eu or hypothesis_af or hypothesis_as or hypothesis_oc:
    label = "contradiction"
elif all([hypothesis_na, hypothesis_eu, hypothesis_af, hypothesis_as, hypothesis_oc]):
    # the hypothesis values are consistent with the premise values, so we can infer entailment
    label = "entailment"
else:
    # the premise values and hypothesis values do not contradict, but we cannot infer entailment
    label = "neutral"

print(label)
