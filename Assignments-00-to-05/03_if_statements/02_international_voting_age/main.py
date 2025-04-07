def check_voting_eligibility(age):
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }
    
    for country, voting_age in voting_ages.items():
        if age >= voting_age:
            print(f"You can vote in {country} where the voting age is {voting_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {voting_age}.")

def main():
    age = int(input("How old are you? "))
    check_voting_eligibility(age)

if __name__ == "__main__":
    main()