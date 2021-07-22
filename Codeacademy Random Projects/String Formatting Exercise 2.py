# String Formatting Exercise 2

# The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

# Run poem_description with the following arguments and save the results to the variable my_beard_description:

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

# Running the variable --- my_beard_description
my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

#------------------
#-------------

# [1]
# Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

# [2]
# The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication. Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

# [3]
# Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up. Start by creating a new empty list, highlighted_poems_stripped.

# Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)

# [4]
# Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists. Create a new empty list called highlighted_poems_details

highlighted_poems_details = []

# [5] 
# Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details

for detail in highlighted_poems_stripped:
  highlighted_poems_details.append(detail.split(':'))

print(highlighted_poems_details)

# [6] 
# Now we want to separate out all of the titles, the poets, and the publication dates into their own lists. Create three new empty lists, titles, poets, and dates

titles = []
poets  = []
dates  = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

print(titles)
print(poets)
print(dates)

# [7] 
# Finally, write a for loop that uses .format() to print out the following string for each poem:
# The poem TITLE was published by POET in DATE

def poem(title, poets, dates):
    return "The poem {titles} was published by {poets} in {dates}.".format(titles=titles, poets=poets, dates=dates)