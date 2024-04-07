# Premise: Two other marines, Tyler Jackson and John Jodka III, have already pleaded guilty to aggravated assault and conspiracy to obstruct justice and were sentenced to 21 months and 18 months, respectively.
# Hypothesis: Tyler Jackson has been sentenced to 18 months.
# Golden Label: neutral

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

