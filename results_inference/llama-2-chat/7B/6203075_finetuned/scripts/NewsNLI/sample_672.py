snow_inch_ urbana_premise = 9
snow_inch_ohare_premise = 3.9
snow_inch_detroit_hypothesis = 5.5

# the hypothesis mentions the snow inch at O'Hare Airport and Detroit, which are also mentioned in the premise
# however, the hypothesis mentions a different amount of snow inch for O'Hare Airport than in the premise
if snow_inch_ohare_premise!= snow_inch_detroit_hypothesis:
    # check if the snow inch at O'Hare Airport in the hypothesis contradicts the snow inch reported in the premise
    label = "contradiction"
else:
    # if the snow inch at O'Hare Airport in the hypothesis does not contradict the snow inch reported in the premise, we can infer entailment
    label = "entailment"

print(label)
