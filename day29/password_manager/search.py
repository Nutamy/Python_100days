with open("data.txt", "r") as file:
    data = file.read().splitlines()

clean_data = {}

for row in data:
    if len(row) > 1:
        parts = row.split(" | ")
        clean_data[parts[0]] = {
            "email": parts[1],
            "password": parts[2]
        }


def searching(site):
    try:
        result = clean_data[site]
    except:
        return "There is nothing"
    else:
        email = result["email"]
        password = result["password"]
        return f"Email: {email}\nPassword: {password}"
