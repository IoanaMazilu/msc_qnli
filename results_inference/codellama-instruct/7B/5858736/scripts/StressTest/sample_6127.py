iceland_visitors_premise = 41
iceland_visitors_hypothesis = 31
norway_visitors_premise = 41
norway_visitors_hypothesis = 31

# the hypothesis refers to the number of visitors to both Iceland and Norway, mentioned in the premise
if iceland_visitors_hypothesis <= iceland_visitors_premise and norway_visitors_hypothesis <= norway_visitors_premise:
    # check if the estimate of 'iceland_visitors_hypothesis' and 'norway_visitors_hypothesis' contradicts the number of visitors to both countries reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
