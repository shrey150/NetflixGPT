# get the section named "Plot" from `page`
# section = page.getSection("Plot")

# item = pywikibot.ItemPage.fromPage(page).get()
# print("BRUH", item)

# parse out the section starting with ** Plot **
section = page.text.split("== Plot ==")[1].split("==")

# set up a LangChain openAI model
llm = ChatOpenAI(model_name = 'gpt-3.5-turbo')

# use the model to pass in page.text and get the plot summary
res = llm(f"Extract a plot summary from the following text: {page.text}")
print(res)


print("SECTION", section)

exit()


# search Wikipedia for "{ep_title} ({title})"
def search_wiki(title, ep_title):
    res = wiki.page(f"{ep_title} ({title})")
    print('AND THE RESULT:', res)
    print(res.title, res.html())
    print(res.content)
    return
    print(res.categories)
    print(res.sections)
    print(res.summary)

search_wiki(title, ep_title)