# The hypothesis refers to the number of rubies in the treasure chest
# The premise gives the total number of gems and the number of diamonds

# The hypothesis states that 5108.0 of the gems were rubies
# The premise gives the total number of rubies as 45.0

if 5108.0!= 45.0:
    # check if the number of rubies in the hypothesis contradicts the number of rubies in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values match, we can infer entailment
    label = "entailment"

print(label)
