import subprocess
import os
git_name = os.environ.get('GIT_NAME')
git_email = os.environ.get('GIT_EMAIL')
if git_email is None or git_name is None:
    raise Exception('Environment variables required: GIT_NAME, GIT_EMAIL')

subprocess.check_output(["git", "config", "--global", "user.name", git_name], stderr=subprocess.STDOUT)
print(f'Git user.name was set as {git_name}')
subprocess.check_output(["git", "config", "--global", "user.email", git_email], stderr=subprocess.STDOUT)
print(f'Git user.email was set as {git_email}')
