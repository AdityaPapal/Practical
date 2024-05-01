class HelpDeskExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "issue": {
                "printer": {
                    "error_message": "Printer is not responding",
                    "solutions": [
                        "Check if the printer is turned on.",
                        "Make sure the printer is connected to the computer.",
                        "Restart the printer and try again."
                    ]
                },
                "network": {
                    "error_message": "Cannot connect to the network",
                    "solutions": [
                        "Check if the network cable is plugged in properly.",
                        "Restart the router or modem.",
                        "Contact the network administrator for further assistance."
                    ]
                },
                "software": {
                    "error_message": "Software application is crashing",
                    "solutions": [
                        "Update the software to the latest version.",
                        "Check if the computer meets the minimum system requirements.",
                        "Reinstall the software and try again."
                    ]
                }
            }
        }

    def get_solution(self, issue_type):
        if issue_type in self.knowledge_base["issue"]:
            error_message = self.knowledge_base["issue"][issue_type]["error_message"]
            solutions = self.knowledge_base["issue"][issue_type]["solutions"]
            return error_message, solutions
        else:
            return "Issue type not found in the knowledge base.", []

# Example usage:
expert_system = HelpDeskExpertSystem()

print("Welcome to the Help Desk Expert System!")
print("Please select the type of issue you are facing:")
print("1. Printer issue")
print("2. Network issue")
print("3. Software issue")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    issue_type = "printer"
elif choice == '2':
    issue_type = "network"
elif choice == '3':
    issue_type = "software"
else:
    print("Invalid choice.")
    exit()

error_message, solutions = expert_system.get_solution(issue_type)
print("\nError message:", error_message)
print("Possible solutions:")
for i, solution in enumerate(solutions, 1):
    print(f"{i}. {solution}")
