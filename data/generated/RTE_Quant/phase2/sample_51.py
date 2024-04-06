# Premise: More than 1,000 members of the Russian and foreign media registered for the news conference, which has become an annual event.
# Hypothesis: More than 1,000 members from Russia registered for the news conference.
# Golden Label: neutral

total_members_premise = 1000
russian_members_hypothesis = 1000

# the hypothesis talks about the number of Russian members which are not referenced in the premise (the nationality of the members is not mentioned)
# the hypothesis cannot be entailed from the premise, since the number of Russian members is unknown.
label = "neutral"

print(label)

