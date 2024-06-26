snow_urbana = 9
snow_ohare = 3.9
snow_detroit = 5.5

# the hypothesis mentions the snowfall at O'Hare Airport and Detroit, which are also mentioned in the premise
if snow_ohare!= snow_urbana:
    # check if the snowfall at O'Hare Airport in the hypothesis contradicts the snowfall at Urbana in the premise
    label = "contradiction"
elif snow_detroit!= snow_urbana:
    # check if the snowfall at Detroit in the hypothesis contradicts the snowfall at Urbana in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
