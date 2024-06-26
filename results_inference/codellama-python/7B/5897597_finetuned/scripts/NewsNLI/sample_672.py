snow_urbana_premise = 9
snow_ohare_premise = 3.9
snow_detroit_hypothesis = 5.5

# the hypothesis mentions the snowfall at O'Hare Airport and Detroit, which are also mentioned in the premise
if snow_ohare_premise!= snow_detroit_hypothesis:
    # check if the snowfall at O'Hare Airport from the hypothesis contradicts the snowfall at Detroit in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
