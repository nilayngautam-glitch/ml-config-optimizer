import requests
repo_link = input("Enter the link of the repo : ")

link_split = repo_link.split("/")

owner = link_split[3]
repo_name = link_split[4]

response = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}")
file = response.json()

def print_section(title):
    line = "=" * len(title)
    print(f"\n{line}\n{title}\n{line}\n")

print_section("Description")
print(f"{file["description"]}\n")

print_section("Language")
print(f"{file["language"]}\n")

print_section("Topics")
print(f"{file["topics"]}\n")

print_section("Size")
print(f"{file["size"]}\n")

print_section("Watchers Count")
print(f"{file["watchers_count"]}\n")

