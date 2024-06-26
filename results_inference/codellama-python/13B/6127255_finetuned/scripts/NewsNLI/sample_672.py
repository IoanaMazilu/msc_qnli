snow_inch_urbana_premise = 9
snow_inch_ohare_premise = 3.9
snow_inch_detroit_hypothesis = 5.5

# the hypothesis mentions the snowfall at O'Hare Airport and Detroit, which are also mentioned in the premise
if snow_inch_ohare_premise!= snow_inch_detroit_hypothesis:
    # check if the snowfall at O'Hare Airport in the hypothesis contradicts the snowfall reported in Chicago (O'Hare Airport) in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
