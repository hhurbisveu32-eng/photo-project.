import requests

# 1. Replace this with your actual Discord Webhook URL
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"

# 2. This is the direct link to your photo
IMAGE_URL = "https://www.lifeloveandsugar.com/wp-content/uploads/2014/06/Strawberry-Shortcake-Cheesecake3.jpg"

# 3. Create the payload with an 'embed'
# Putting the link in the 'image' field is what makes it 'show' the photo
payload = {
    "username": "Image Logger Bot",
    "embeds": [
        {
            "title": "New Image Logged!",
            "description": "The cheesecake photo is showing below:",
            "color": 15277667,  # This is a pinkish color
            "image": {
                "url": IMAGE_URL
            },
            "footer": {
                "text": "Assignment Submission"
            }
        }
    ]
}

# 4. Send the request to Discord
response = requests.post(WEBHOOK_URL, json=payload)

# 5. Check if it worked
if response.status_code == 204:
    print("Success! Check your Discord channel.")
else:
    print(f"Failed to send. Error code: {response.status_code}")
