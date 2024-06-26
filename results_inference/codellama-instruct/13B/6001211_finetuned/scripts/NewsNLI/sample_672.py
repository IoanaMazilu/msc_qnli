snow_inches_Urbana = 9
snow_inches_OHARE = 3.9
snow_inches_Detroit = 5.5

# the hypothesis mentions the snowfall at O'Hare Airport and Detroit, which are also mentioned in the premise
if snow_inches_OHARE!= snow_inches_OHARE:
    # check if the snowfall at O'Hare Airport in the hypothesis contradicts the snowfall reported in the premise
    label = "contradiction"
elif snow_inches_Detroit > snow_inches_Detroit:
    # check if the snowfall in Detroit from the hypothesis contradicts the snowfall in Detroit in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
