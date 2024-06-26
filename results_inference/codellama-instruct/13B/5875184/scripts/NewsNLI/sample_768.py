premise = "Flare with Fin-X technology is the name of a new range of saucepans that claim to cook 40% faster than traditional pans, thus saving both time and energy."
hypothesis = "Futuristic saucepans can cook food 40% faster than our traditional utensils."

# extract the numerical information from the premise
premise_speedup = 0.4

# extract the numerical information from the hypothesis
hypothesis_speedup = 0.4

# compare the speedup values
if premise_speedup!= hypothesis_speedup:
    # check if the speedup in the hypothesis contradicts the speedup reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
