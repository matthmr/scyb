# SCYB - Simple Channel `ytInitialData` Browser

A simple localhost-based browser for `ytInitialData` given a channel id.

## Usage

Download a CSV list of channels your youtube account is subscribed to:

1. go to [your account's
   Google takeout](https://takeout.google.com/takeout/custom/youtube)
2. click the *All YouTube data included* button, then unmark all but
   *subscriptions*
3. click *Next step*, then click *Create export*
4. download the zip file from your account's email address
5. unzip the file, then copy `./Takeout/YouTube and YouTube
   Music/subscriptions/subscriptions.csv` into this directory

Once you have you CSV file in this directory, run `./gen_site.sh`.

Run `./server.py` **with this directory as the working directory (cwd)**. That
will open a connection in `localhost` with port 8080.

Open a browser with javacript enabled (any modern-ish browser should do), then
connect to `http://localhost:8080`.
