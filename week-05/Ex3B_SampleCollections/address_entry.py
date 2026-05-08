contact_info = {
    "name": "ndifon caleb",
    "address": "102 castle",
    "city": "wilmington",
    "state": "DE",
    "zip": "17253",
}

print(f"""{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")


contact_info = {
    "address": "102 castle",
    "city": "wilmington",
    "state": "DE",
    "zip": "17253",
}


full_name = {
    "first name": "ndifon",
    "last name": "caleb"
}


full_name.update({
    "honorific": "prof."
})


contact_info.update({
    "full_name": full_name
})

title = full_name["honorific"]
first = full_name["first name"]
last = full_name["last name"]

print(f"""{title} {first} {last}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")