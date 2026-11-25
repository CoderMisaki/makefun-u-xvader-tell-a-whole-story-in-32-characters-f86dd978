"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name (32 characters or fewer) to
/output/entry.txt. Python standard library only.
"""

import os

WIFI_NAME = "The WiFi died during my proposal"


def main() -> None:
    # One network name, no trailing newline: the gate counts every
    # character, so the file holds exactly the name and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WIFI_NAME)


if __name__ == "__main__":
    main()
