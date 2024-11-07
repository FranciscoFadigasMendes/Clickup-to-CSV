import requests
import csv

# Replace with your API token and list ID
API_TOKEN = 'pk_88710984_GPU82FQ1W3H9CPDDVC67H0KQINS0BPJC'
ID = 901507004313

url = f'https://api.clickup.com/api/v2/list/{ID}/task'

headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json'
}

#--------------------------------------------------------

# Step 1: Get the task data
response = requests.get(url, headers=headers)

# Step 2: Debugging: Check the entire response
if response.status_code == 200:
    try:
        data = response.json()
        #print(data)  # Print the entire JSON response to inspect its structure

        # Safely get 'tasks' key or an empty list if not found
        tasks = data.get("tasks", [])

        if tasks:
            # Step 3: Define the CSV file and write the header
            with open("clickup_tasks.csv", mode="w", newline="") as csv_file:
                fieldnames = ["id", "name", "status", "due_date", "priority", "assignees"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                # Step 4: Write each task's information to the CSV file
                for task in tasks:
                    # Process assignees as a list of names
                    assignees = ", ".join([assignee["username"] for assignee in task.get("assignees", [])])

                    # Write each row
                    writer.writerow({
                        "id": task.get("id"),
                        "name": task.get("name"),
                        "status": task.get("status", {}).get("status", "N/A"),
                        "due_date": task.get("due_date", "N/A"),
                        "priority": task.get("priority", "N/A"),
                        "assignees": assignees
                    })

            print("Tasks have been written to clickup_tasks.csv")
        else:
            print("No tasks found in the response.")
    except Exception as e:
        print(f"Error processing the response: {e}")
else:
    print(f"Error: {response.status_code}, {response.text}")

print("DONE - API to JSON to CSV")
