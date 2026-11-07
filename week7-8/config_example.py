# config_example.py — TEMPLATE, not your real config.
#
# Your API key is a secret, like a password. If it's written directly inside
# weather.py and you push that file to GitHub, anyone can see it and use your
# account. The fix: keep the real key in its own file called config.py, and
# never commit that file (see week7-8/README.md step 3 and the .gitignore
# step when you create your own repo).
#
# To use this:
#   1. Make a copy of this file in the same folder.
#   2. Rename the copy to exactly: config.py
#   3. Replace the placeholder below with your real key.
#
# config.py is already excluded from git in this repo's .gitignore. When you
# move this project into its own repo later, you'll add that same rule there.

API_KEY = "YOUR_API_KEY_HERE"
