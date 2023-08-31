import requests

# Define Postman API endpoint
postman_api_endpoint = 'postman endpoint url here'  # Replace with the actual Postman API URL

# Make a request to the Postman API
response = requests.get(postman_api_endpoint, verify=False)  # Disabling SSL verification

if response.status_code == 200:
    try:
        # Parse the response to extract data
        api_data = response.json()

        # Extract data directly from the 'data' object
        data = api_data.get('data', {})
        ping = round(data.get('ping', 0), 2)  # Round to 2 decimal places
        download = round(data.get('download', 0), 2)
        upload = round(data.get('upload', 0), 2)
        server_name = data.get('server_name', '')

        # Construct payload for Discord webhook
        payload = {
            'content': None,
            'embeds': [
                {
                    'title': '**Speed Test Results**',
                    'description': f"**Server**: {server_name}\n\n",
                    'color': 0xFFA500,  # Use a color code for the embed (orange)
                    'fields': [
                        {'name': 'Ping', 'value': f'{ping} ms', 'inline': True},
                        {'name': 'Download', 'value': f'{download} Mbps', 'inline': True},
                        {'name': 'Upload', 'value': f'{upload} Mbps', 'inline': True}
                    ]
                }
            ]
        }

        # Send payload to Discord webhook
        discord_webhook_url = 'discord webhook url here'
        discord_response = requests.post(discord_webhook_url, json=payload)

        if discord_response.status_code == 204:
            print('Webhook message sent successfully.')
        else:
            print('Error sending webhook message:', discord_response.text)
    except Exception as e:
        print('Error processing API response:', e)
else:
    print('Error accessing Postman API:', response.status_code)
