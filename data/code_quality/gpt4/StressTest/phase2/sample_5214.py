boys_percentage_premise = 50
boys_percentage_hypothesis = 30

# the hypothesis speaks about the percentage of boys in the total school population, also mentioned in the premise
if boys_percentage_hypothesis >= boys_percentage_premise:
    # check if the hypothesis value contradicts the percentage of boys in the premise
    label = "contradiction"
elif boys_percentage_hypothesis < boys_percentage_premise:
    # any percentage of boys less than 'boys_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
