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

3. Generate an _**Access Token**_ and paste it in [line 3 of scipt.py](https://github.com/NotBot-Automation-Bots/Get-Messenger-Chat-History/blob/3404def9eeee435d4e600a3feae2ebcf8699855f/script.py#L3) (replace the string **your-page-access-token** with the generated token).

8. `python3 script.py`