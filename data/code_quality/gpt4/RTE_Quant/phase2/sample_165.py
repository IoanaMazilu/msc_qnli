# Defining the variables
tyler_sentence_premise = 21
john_sentence_premise = 18
tyler_sentence_hypothesis = 18

# Comparing the sentences of Tyler from the premise and the hypothesis
if tyler_sentence_hypothesis != tyler_sentence_premise:
    # If the sentences do not match, it is a contradiction
    label = "contradiction"
else:
    label = "entailment"
    
print(label)
