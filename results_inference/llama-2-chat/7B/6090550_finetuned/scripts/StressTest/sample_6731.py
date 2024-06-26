, #given_oranges_premise, #given_oranges_hypothesis

#given_oranges_premise = 50
#given_oranges_hypothesis = 40

#oranges_to_keep_premise = #given_oranges_premise
#oranges_to_keep_hypothesis = #given_oranges_hypothesis

#average_price_premise = 50
#average_price_hypothesis = 40

#contradiction_premise = 0
#contradiction_hypothesis = 0

#entailment_premise = 1
#entailment_hypothesis = 1

#neutral_premise = 0
#neutral_hypothesis = 0

#average_price_premise!= average_price_hypothesis
#oranges_to_keep_premise!= oranges_to_keep_hypothesis

#if #average_price_premise!= #average_price_hypothesis:
#    #contradiction_premise = 1
#    #contradiction_hypothesis = 1
#elif #oranges_to_keep_premise!= #oranges_to_keep_hypothesis:
#    #entailment_premise = 1
#    #entailment_hypothesis = 1
#else:
#    #neutral_premise = 1
#    #neutral_hypothesis = 1

#print(f"{#contradiction_premise} - #contradiction_hypothesis")
#print(f"{#entailment_premise} - #entailment_hypothesis")
#print(f"{#neutral_premise} - #neutral_hypothesis")

