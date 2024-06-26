premise_kidnappings = 15
premise_beheadings = 3
hypothesis_kidnappings = 15
hypothesis_beheadings = 0

# the hypothesis talks about the number of kidnappings, which is mentioned in the premise
if hypothesis_kidnappings!= premise_kidnappings:
    # check if the number of kidnappings in the hypothesis contradicts the number of kidnappings from the premise
    label = "contradiction"
elif hypothesis_beheadings!= premise_beheadings:
    # check if the number of beheadings in the hypothesis contradicts the number of beheadings from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
