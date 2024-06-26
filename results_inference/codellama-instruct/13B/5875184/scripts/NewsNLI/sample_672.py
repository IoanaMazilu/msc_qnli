snow_premise = 9
snow_hypothesis = 3.9

# the hypothesis mentions the snowfall at O'Hare Airport, which is also mentioned in the premise
if snow_hypothesis!= snow_premise:
    # check if the snowfall at O'Hare Airport contradicts the snowfall reported in the premise
    label = "contradiction"
else:
    # if the snowfall at O'Hare Airport does not contradict the snowfall in the premise, we can infer entailment
    label = "entailment"

print(label)
