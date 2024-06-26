premise_random_processing = 112
premise_scramjet_rocket_engines = 234
premise_both = 112

hypothesis_random_processing = 312
hypothesis_scramjet_rocket_engines = 234
hypothesis_both = 112

# the hypothesis refers to the number of students studying Random-processing methods and Scramjet rocket engines
if hypothesis_random_processing <= premise_random_processing and hypothesis_scramjet_rocket_engines <= premise_scramjet_rocket_engines:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif hypothesis_both!= premise_both:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
