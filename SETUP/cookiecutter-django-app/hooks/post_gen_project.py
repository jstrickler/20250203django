from django.core.management.utils import get_random_secret_key
import shutil
import os

app_config = "    '%s.apps.%sConfig'," % ("{{ cookiecutter.app_slug }}", "{{cookiecutter.app_slug.title()}}")

current_folder = os.getcwd()
project_name = os.path.basename(os.path.dirname(current_folder))
settings_path = '../config/settings/dev.py'
print(f"{os.getcwd() = }")


temp_path = settings_path + ".tmp"
backup_path = settings_path + ".bak"
print(f"{current_folder = }")
print(f"{settings_path = }")


with open(settings_path) as settings_in:
    with open(temp_path, "w") as settings_out:
        for line in settings_in:
            settings_out.write(line)
            if "add your apps here" in line:
                settings_out.write(app_config + '\n')

shutil.move(settings_path, backup_path)
shutil.move(temp_path, settings_path)

print(f"""
Adding {app_config} to {settings_path}
""")
