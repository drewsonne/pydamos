import pydamos

for site in pydamos.sites():
    for item in site.items():
        print("Site: '{site}', Item: '{item}'\n\n".format(
            site=site.value,
            item=item.item_name
        ))

for key, facet in pydamos.facets():
    print(key, facet)
