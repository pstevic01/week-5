import copy

# Week 5 - If Statements Assignment

# Step 1: Create a single list that contains the collection of data in the order provided

employee_info_list = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]


# Step 2: Removing bool values and converting employee info list to list of employee dictionaries

updated_employee_list = [item for item in employee_info_list if not isinstance(item, bool)]
parsed_employees = []
i = 0

while i < len(updated_employee_list) - 2:
    triplet = updated_employee_list[i:i+3]
    id = name = wage = None

    for item in triplet:
        if isinstance(item, int) and id is None:
            id = item
        elif isinstance(item, str) and name is None:
            name = item
        elif isinstance(item, float) and wage is None:
            wage = item

    if id is not None and name is not None and wage is not None:
        parsed_employees.append({
            "id": id,
            "name": name,
            "hourly_rate": wage
        })
        i += 3
    else:
        i += 1


# Step 3: Removeing duplicates 

unique_employees = []
identifier_found = set()

for employee in parsed_employees:
    identifier = (employee["id"], employee["name"], employee["hourly_rate"])
    if identifier not in identifier_found:
        identifier_found.add(identifier)
        unique_employees.append(employee)


# Step 4: Add total_hourly_rate and multiply the hourly rate by 1.3 

total_hourly_rate = []

for employee in unique_employees:
    total_rate = round(employee["hourly_rate"] * 1.3, 2)
    employee["total_hourly_rate"] = total_rate
    total_hourly_rate.append({
        "id": employee["id"],
        "name": employee["name"],
        "total_hourly_rate": total_rate
    })


# Step 5: Create a list of underpaid employees with pay rates between 28.15 to 30.65

underpaid_salaries = []

for employee in unique_employees:
    if 28.15 <= employee["total_hourly_rate"] <= 30.65:
        underpaid_salaries.append({
            "id": employee["id"],
            "name": employee["name"],
            "total_hourly_rate": employee["total_hourly_rate"]
        })

# Step 6: Apply raises based on hourly rate brackets

company_raises = []

for employee in unique_employees:
    rate = employee["hourly_rate"]
    if 22 <= rate < 24:
        raise_amt = round(rate * 0.05, 2)
    elif 24 <= rate < 26:
        raise_amt = round(rate * 0.04, 2)
    elif 26 <= rate < 28:
        raise_amt = round(rate * 0.03, 2)
    else:
        raise_amt = round(rate * 0.02, 2)

    employee["raise_amount"] = raise_amt
    company_raises.append({
        "name": employee["name"],
        "raise_amount": raise_amt
    })

# Step 7: Print outputs

print("\nEmployees with their hourly rates:")
for employee in total_hourly_rate:
    print(employee)

print("\nEmployees with total hourly rate between $28.15 and $30.65:")
for employee in underpaid_salaries:
    print(employee)

print("\nEmployee raises:")
for employee in company_raises:
    print(employee)