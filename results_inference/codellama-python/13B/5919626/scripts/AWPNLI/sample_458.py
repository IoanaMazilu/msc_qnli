man_height = 1.75
woman_height = 1.62

# the hypothesis talks about the height of the man, which is also referenced in the premise
# check if the man is taller than the woman
if man_height > woman_height:
    # check if the man is taller than the woman
    label = "entailment"
else:
    # if the man is not taller than the woman, we can infer contradiction
    label = "contradiction"
    
print(label)
