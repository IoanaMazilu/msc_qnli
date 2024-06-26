snow_inch_premise_urbana = 9
snow_inch_premise_ohare = 3.9
snow_inch_hypothesis_detroit = 5.5

# the hypothesis mentions the snow inch at O'Hare Airport, which is also mentioned in the premise
if snow_inch_hypothesis_detroit!= snow_inch_premise_ohare:
    # check if the snow inch at O'Hare Airport in the hypothesis contradicts the snow inch reported in the premise
    label = "contradiction"
elif snow_inch_premise_urbana!= 9:
    # check if the snow inch reported in Urbana, Illinois contradicts the snow inch reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
