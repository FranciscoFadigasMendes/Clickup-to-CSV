import requests
import csv

# Replace with your API token and list ID
API_TOKEN = 'your_api_token_here'
LIST_ID = 'your_list_id_here'

url = f'https://api.clickup.com/api/v2/list/{LIST_ID}/task'

headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json'
}

# Step 1: Get the task data
response = requests.get(url, headers=headers)

if response.status_code == 200:
    tasks = response.json()["tasks"]

    # Step 2: Define the CSV file and write the header
    with open("clickup_tasks.csv", mode="w", newline="") as csv_file:
        fieldnames = ["id", "name", "status", "due_date", "priority", "assignees"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Step 3: Write each task's information to the CSV file
        for task in tasks:
            # Process assignees as a list of names
            assignees = ", ".join([assignee["username"] for assignee in task.get("assignees", [])])

            # Write each row
            writer.writerow({
                "id": task.get("id"),
                "name": task.get("name"),
                "status": task.get("status", {}).get("status"),
                "due_date": task.get("due_date"),
                "priority": task.get("priority"),
                "assignees": assignees
            })

    print("Tasks have been written to clickup_tasks.csv")
else:
    print("Error:", response.status_code, response.text)

print("DONE - API to JSON to CSV")
