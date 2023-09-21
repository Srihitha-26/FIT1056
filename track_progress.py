# # def notify_user(achievement):
# #     print(f"Congratulations! You've earned the '{achievement}' achievement.")
#
# from user_registration import login_user
#
#
# class track_progress:
#     def __init__(self):
#         self.achievements = {
#             "Module Completed": {"type": "module", "criteria": 1},
#             "Task Master": {"type": "task", "criteria": 5},
#         }
#         self.user_progress = {
#             "modules_completed": 0,
#             "tasks_completed": 0,
#         }
#
#     def complete_module(self):
#         self.user_progress["modules_completed"] += 1
#         self.check_achievements()
#
#     def complete_task(self):
#         self.user_progress["tasks_completed"] += 1
#         self.check_achievements()
#
#     def check_achievements(self, username, password):
#         # Add code to check user credentials here
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if login_user(username, password):
#             earned_achievements = []
#
#             for achievement, info in self.achievements.items():
#                 if (
#                         info["type"] == "module"
#                         and self.user_progress["modules_completed"] >= info["criteria"]
#                 ):
#                     earned_achievements.append(achievement)
#                 elif (
#                         info["type"] == "task"
#                         and self.user_progress["tasks_completed"] >= info["criteria"]
#                 ):
#                     earned_achievements.append(achievement)
#
#             if earned_achievements:
#                 print("Earned Achievements:")
#                 for achievement in earned_achievements:
#                     print(f"- {achievement}")
#             else:
#                 print("You have not earned any achievements yet.")
#         else:
#             print("Invalid username or password. Achievements cannot be checked.")
#
#
# def check_achievements():
#     return None

class track_progress:
    def __init__(self, progress_file='user_progress.txt'):
        self.progress_file = progress_file
        self.achievements = {
            "Module Completed": {"type": "module", "criteria": 1},
            "Task Master": {"type": "task", "criteria": 5},
        }
        self.user_progress = {
            "modules_completed": 0,
            "points earned": 0,
        }

    def update_progress(self, username, password, modules_completed, tasks_completed):
        with open(self.progress_file, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        user_found = False

        for line in lines:
            parts = line.strip().split(',')
            if parts[0] == username and parts[1] == password:
                user_found = True
                updated_line = f"{username},{modules_completed},{tasks_completed}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)

        if not user_found:
            new_line = f"{username},{password}, {modules_completed},{tasks_completed}\n"
            updated_lines.append(new_line)

        with open(self.progress_file, 'w') as file:
            file.writelines(updated_lines)

    def get_user_progress(self, username, password):
        with open(self.progress_file, 'r') as file:
            lines = file.readlines()

        for line in lines[1:]:  # Skip the header line
            parts = line.strip().split(',')
            if parts[0] == username and parts[1] == password:
                return {
                    'modules_completed': int(parts[2]),
                    'points earned': int(parts[3])
                    }

        return None
