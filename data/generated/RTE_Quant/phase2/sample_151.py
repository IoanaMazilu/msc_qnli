# Premise: Two portraits, one by Reynolds, the other by Gainsborough, since 1990 among the most looked-after works in the Art Loss Register database, were recovered this week when they were brought into Sotheby's for evaluation. Also a lithograph by Norwegian artist Edvard Munch, stolen from an Oslo art gallery in April, has been recovered, news reports said today.
# Hypothesis: These two portraits and a lithography by Edvard Munch were recovered using the Art Loss Register database.
# Golden Label: neutral

portraits_premise = 2
portraits_hypothesis = 2
lithography_premise = 1
lithography_hypothesis = 1
year_premise = 1990
year_hypothesis = None

# the hypothesis states the number of recovered portraits and a lithography, which is also mentioned in the premise
if portraits_hypothesis != portraits_premise:
    # check if the number of recovered portraits in the hypothesis contradicts the number of portraits from the premise
    label = "contradiction"
elif lithography_hypothesis != lithography_premise:
    # check if the number of recovered lithographs in the hypothesis contradicts the number of lithographs from the premise
    label = "contradiction"
# the hypothesis suggests that the Art Loss Register database was used to recover the portraits and lithograph, but the premise does not specify the method of recovery
# the hypothesis cannot be fully and explicitly entailed from the premise
else:
    label = "neutral"

print(label)

