import os
import requests
import re
import time

# --- SETTINGS ---
# Replace with your generated token
GITHUB_TOKEN = "SEU_TOKEN_AQUI"
BASE_URL = "https://api.github.com/repos"
OUTPUT_DIR = "analise_pr_ros2"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# List of PRs you want to analyze
# Add as many links as you want here
lista_de_pull_requests = [
    "https://github.com/ros2/rosidl_python/pull/35",
    "https://github.com/ros2/rclcpp/pull/628",
    "https://github.com/ros2/rclcpp/pull/690",
    "https://github.com/ros2/launch_ros/pull/9",
    "https://github.com/eProsima/Fast-DDS/pull/332",
    "https://github.com/ros2/rcl/pull/366",
    "https://github.com/ros2/rosidl/pull/333",
    "https://github.com/ros2/rmw_implementation/pull/51",
    "https://github.com/ros2/rcl/pull/418",
    "https://github.com/ament/ament_cmake/pull/187",
    "https://github.com/colcon/colcon-core/pull/209",
    "https://github.com/ros2/rmw_cyclonedds/pull/60",
    "https://github.com/ros2/rclcpp/pull/873",
    "https://github.com/ros2/rmw_cyclonedds/pull/53",
    "https://github.com/ApexAI/performance_test/pull/75",
    "https://github.com/ros-navigation/navigation2/pull/1057",
    "https://github.com/ros2/sros2/pull/126",
    "https://github.com/ros2/sros2/pull/138",
    "https://github.com/ros2/sros2/pull/140",
    "https://github.com/eProsima/Fast-DDS/pull/632",
    "https://github.com/eclipse-cyclonedds/cyclonedds/pull/222",
    "https://github.com/ros2/rosbag2/pull/308",
    "https://github.com/ros2/rosbag2/pull/529",
    "https://github.com/ros2/launch_ros/pull/311",
    "https://github.com/ros2/rclcpp/pull/2030",
    "https://github.com/ros2/rclcpp/pull/2032",
    "https://github.com/ros2/rosbag2/pull/1457",
    "https://github.com/ros2/rosbag2/pull/1516",
    "https://github.com/ros-visualization/rqt_bag/pull/156"
]


def download_file(url, path):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(response.content)
        elif response.status_code == 404:
            print(f"      [!] File not found (404) at: {url}")
    except Exception as e:
        print(f"      [!] Error downloading: {e}")


def process_pull_request(pr_url):
    match = re.search(r"github\.com/([\w-]+)/([\w-]+)/pull/(\d+)", pr_url)
    if not match:
        print(f"\n[X] Invalid URL: {pr_url}")
        return

    owner, repo, pr_number = match.groups()
    print(f"\n--- Processing {repo} PR #{pr_number} ---")

    # 1. Get PR data
    pr_resp = requests.get(f"{BASE_URL}/{owner}/{repo}/pulls/{pr_number}", headers=headers)
    if pr_resp.status_code != 200:
        print(f"    Error accessing API: {pr_resp.status_code}")
        return

    pr_data = pr_resp.json()
    base_sha = pr_data['base']['sha']
    head_sha = pr_data['head']['sha']

    print(f"    Base SHA (Before): {base_sha[:7]}")
    print(f"    Head SHA (After): {head_sha[:7]}")

    # 2. List files
    files_url = f"{BASE_URL}/{owner}/{repo}/pulls/{pr_number}/files"
    files = requests.get(files_url, headers=headers).json()

    for file in files:
        filename = file['filename']
        status = file['status']

        # We create specific folders for each PR and each state
        folder_path = os.path.join(OUTPUT_DIR, f"pr_{pr_number}")
        path_before = os.path.join(folder_path, "before", filename)
        path_after = os.path.join(folder_path, "after", filename)

        print(f"    -> Downloading: {filename} ({status})")

        # AFTER version
        if status != "removed":
            head_file_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{head_sha}/{filename}"
            download_file(head_file_url, path_after)

        # BEFORE version
        if status != "added":
            base_file_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{base_sha}/{filename}"
            download_file(base_file_url, path_before)

    # Short pause to respect API rate limits (best practice)
    time.sleep(1)


# Main loop
if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for url in lista_de_pull_requests:
        process_pull_request(url)

    print("\n" + "=" * 30)
    print("Processing finished!")
