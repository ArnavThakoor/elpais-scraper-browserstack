import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

USERNAME = "arnavthakoor_GJneZg"
ACCESS_KEY = "qvUfX7taDGVxnzGwy4fz"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# 5 parallel devices/browsers
CAPABILITIES = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Chrome on Windows 11"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "sessionName": "Firefox on Windows 10"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Ventura",
            "sessionName": "Safari on macOS Ventura"
        }
    },
    {
        "browserName": "Safari",
        "bstack:options": {
            "deviceName": "iPhone 14",
            "realMobile": "true",
            "osVersion": "16",
            "sessionName": "iPhone 14 Test"
        }
    },
    {
        "browserName": "Chrome",
        "bstack:options": {
            "deviceName": "Samsung Galaxy S23",
            "realMobile": "true",
            "osVersion": "13",
            "sessionName": "Galaxy S23 Test"
        }
    }
]


def run_test(cap):
    print(f"\n🔵 Starting → {cap['bstack:options']['sessionName']}")

    # Create Options object
    options = ChromeOptions()
    for key, value in cap.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get("https://elpais.com/")
        print("   ✓ Loaded El País")
        print("   ✓ Title:", driver.title)
    except Exception as e:
        print("   ❌ Error:", e)
    finally:
        driver.quit()
        print(f"🔴 Finished → {cap['bstack:options']['sessionName']}")


# Run threads
threads = []

for cap in CAPABILITIES:
    t = threading.Thread(target=run_test, args=(cap,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n🎉 All BrowserStack tests completed.\n")