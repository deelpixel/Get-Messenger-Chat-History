# Get-Messenger-Chat-History
Get Messenger Chat History

## Steps

1. Go to Facebook Graph API Explorer
https://developers.facebook.com/tools/explorer

2. Add all the permissions (including _**pages_read_engagement**_) to the list of permissions.

4. `git clone https://github.com/NotBot-Automation-Bots/Get-Messenger-Chat-History.git`

5. `cd Get-Messenger-Chat-History`

5. `python3 -m venv venv`

6. `source venv/bin/activate`

7. `pip install -r requirements.txt`

3. Generate an _**Access Token**_ and paste it in line 3 of scipt.py (replace the string **PASTE_ACCESS_TOKEN_HERE** with the generated token).
    ```py
    ACCESS_TOKEN = "PASTE_ACCESS_TOKEN_HERE"
    ```

8. `python3 script.py`