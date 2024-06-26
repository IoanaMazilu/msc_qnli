bracelets_hypothesis = 8.0
bracelets_premise = 48.0 / 8.0

# the hypothesis talks about the number of bracelets Shannon can make, which is also referenced in the premise
# compute the number of bracelets Shannon can make from the premise
if bracelets_hypothesis!= bracelets_premise:
    # check if the number of bracelets from the hypothesis contradicts the number of bracelets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
