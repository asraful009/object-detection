import subprocess
import sys


def update_all_packages():
    # Upgrade pip first
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    # Get list of outdated packages
    result = subprocess.run([sys.executable, "-m", "pip", "list", "--outdated"], capture_output=True, text=True)
    outdated_packages = result.stdout.split('\n')[2:-1]  # Skip the header and empty last line

    # Extract package names
    packages_to_update = [package.split()[0] for package in outdated_packages]

    if not packages_to_update:
        print("All packages are up to date!")
        return

    print(f"Updating {len(packages_to_update)} packages:")
    for package in packages_to_update:
        print(f"Updating {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            print(f"{package} updated successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to update {package}. Please update it manually.")

    print("\nAll updates completed. Please check for any warnings or errors above.")


if __name__ == "__main__":
    update_all_packages()