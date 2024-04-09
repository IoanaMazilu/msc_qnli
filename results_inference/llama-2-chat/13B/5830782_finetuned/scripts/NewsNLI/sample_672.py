snow_inches_premise = [3.9, 9]
snow_inches_hypothesis = [3.9, 5.5]

# the hypothesis mentions the amount of snow at O'Hare Airport, which is also mentioned in the premise
if snow_inches_hypothesis[0]!= snow_inches_premise[0]:
    # check if the amount of snow at O'Hare Airport in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the amount of snow at O'Hare Airport in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
