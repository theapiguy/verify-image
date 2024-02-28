import requests

def verify_image_url(image_url):
    try:
        response = requests.head(image_url)  # Send a HEAD request to the URL
        if response.status_code == 200:
            print("Image URL exists.")
        else:
            print(f"Image URL does not exist (Status code: {response.status_code})")
    except requests.ConnectionError:
        print("Could not connect to the server. Please check your internet connection.")
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as e:
        print("An error occurred:", e)

# Check if the Image URL exists
image_url = "[Enter Image URL Here]"
verify_image_url(image_url)
