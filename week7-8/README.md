# Weeks 7–8: AI Weather Mood App

You're going to build a weather app. It fetches real weather for any city and changes
colour based on the mood of the weather.

You do this in five steps, in this exact order. Do not skip ahead.

1. Create an OpenWeatherMap API key
2. Test the key with `curl` — before writing any Python
3. Build the CLI version — `weather.py`
4. Build the UI version — `app.py`
5. Fix the things that go wrong

**Why step 2 exists:** the single biggest reason this project goes wrong is an API key
that isn't working yet — not bad code. `curl` tells you in 10 seconds whether the
problem is your key or your code. Skipping it means you might spend 30 minutes
debugging Python for a problem Python didn't cause.

---

## 1. Create an OpenWeatherMap API key

1. Go to **[openweathermap.org](https://openweathermap.org/)** and click **Sign Up** (top right). It's free — no credit card.
2. Once signed up, click your username (top right) → **My API keys**.
3. You'll see a key already there, under "Key" — a long string of letters and numbers. Copy it.
4. Paste it somewhere safe for now — a plain text file, a sticky note, anywhere you can copy it from again.

> ⏳ **A brand new key can take up to 2 hours to start working.** Usually it's much
> faster — 10 to 20 minutes — but don't assume it's broken just because it doesn't
> work the second you copy it. Move on to step 2 to check it properly. If it's not
> ready yet, come back to it in a while instead of guessing at what's wrong.

**Keep your key private.** Don't post it in chat, don't screenshot it, and don't
type it directly into `weather.py` — step 3 shows you where it actually goes so it
never ends up on GitHub.

---

## 2. Test the key with `curl`

Open the terminal in VS Code — the same terminal you've used all course.

**First, check what kind of terminal you have.** Look at the top-right of the
terminal panel for a label — or just look at the prompt itself. If it says
**PowerShell** or **pwsh** (the default on most Windows computers), follow the
**PowerShell** instructions below. Everyone else (Mac, Linux, Windows Command
Prompt, Git Bash) follows **Everyone else**.

### PowerShell

Plain `curl` in PowerShell is secretly a different tool in disguise (it's an
alias for `Invoke-WebRequest`) and won't behave the way this guide expects.
Use `curl.exe` instead — note the `.exe` — to get the real curl:

```powershell
curl.exe "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY_HERE&units=metric"
```

If `curl.exe` isn't found on your computer, use PowerShell's own command
instead:

```powershell
Invoke-RestMethod "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY_HERE&units=metric"
```

`Invoke-RestMethod` prints the result differently from curl — as a list of
labeled properties instead of one block of text, something like:

```
coord       : @{lon=-0.13; lat=51.51}
weather     : {@{id=800; main=Clear; description=clear sky; icon=01d}}
main        : @{temp=15.2; feels_like=14.6; temp_min=13.9; temp_max=16.1; ...}
name        : London
```

That's still success — look for a `main` property with a `temp` number inside
it. Skip the "What success looks like" box below; this is your version of it.

### Everyone else

```bash
curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY_HERE&units=metric"
```

**What success looks like:** one long line of text starting with `{"coord":` and
containing `"main":{"temp":` somewhere in the middle, with a real number after `temp`.

---

If you saw a `temp` number (in either format above) — your key works. Go to step 3.

If you see something else, use this table before touching any Python:

| You see | What it means | What to do |
|---|---|---|
| `{"cod":401,"message":"Invalid API key..."}` | Key is wrong, or not active yet | Re-copy the key exactly — no extra spaces, no quotes included by accident. If the key is less than 2 hours old, wait and try again. |
| `{"cod":"404","message":"city not found"}` | Your key **works** — the city name is the problem | Not a key issue. Try `q=Toronto` or another real city. |
| `curl: command not found` | Rare — usually an old Windows setup | Make sure you're using the VS Code terminal, not a separate Command Prompt. Ask your teacher if it persists. |
| Output shows `StatusCode`, `StatusDescription`, `Headers`, `Content` instead of JSON | You're in PowerShell and ran plain `curl`, which is really `Invoke-WebRequest` in disguise | Use `curl.exe` (with the `.exe`) or `Invoke-RestMethod` instead — see the PowerShell box above |
| Nothing happens, it just hangs | No internet, or the network is blocking the request | Ask your teacher — this is a network problem, not a code problem. |

Do not open your AI tool and start prompting it until `curl` shows you real weather
data with a `temp` in it. If `curl` doesn't work, your Python won't either, and
you'll waste time thinking your code is broken when it's actually the key.

---

## 3. Build the CLI version — `weather.py`

Your key works now, so the rest of this is just code.

**Install the `requests` library first.** This is the Python package that lets
your code talk to the API, the same job `curl` just did from the terminal. In
the VS Code terminal, run:

```bash
python -m pip install requests
```

If `python` isn't recognized on your computer, use `python3` instead:

```bash
python3 -m pip install requests
```

**Whichever one worked, remember it** — use that exact same word (`python` or
`python3`) every time you install something or run a file for this project,
including later in this guide. Mixing the two is the single most common cause
of "it says requests isn't installed" even right after you installed it —
that happens when `pip` installs requests for one Python, but a different
Python runs your file.

You should see a line ending in `Successfully installed requests-...`. You
only need to install it once on your computer, not every time you run
`weather.py`.

**If you instead see an error containing `externally-managed-environment`, or
a wall of text mentioning SSL / certificates, skip to Section 5 — Fixing
before continuing** — both have exact fixes down there.

Your API key is a secret, like a password. If it ends up written directly inside
`weather.py`, and you later push that file to GitHub, anyone can see it and use
your account. So before writing any code, the key goes in its own file that git
is told to never commit.

**Create your private key file:**

1. In this folder, make a copy of `config_example.py`.
2. Rename the copy to exactly `config.py`.
3. Open `config.py` and replace the placeholder with your real key:
   ```python
   API_KEY = "paste_your_real_key_here"
   ```

That's it — `config.py` is already listed in this repo's `.gitignore`, so git
will never track it or push it anywhere. You'll set up that same protection
again later when you move this project to its own repo (see the last section).

**Now build `weather.py`.** Create an empty file called `weather.py` in this
folder — don't type anything into it yet. The prompt below writes the whole
file for you, and it imports your key from `config.py` instead of containing
the key itself, so nothing secret ever ends up in this file.

Open your AI tool's chat — this could be GitHub Copilot Chat in VS Code, Cursor,
Gemini, ChatGPT, or whatever you're using — and paste this prompt **exactly as
written**, don't paraphrase it. The more exact your prompt, the more your code
will look like everyone else's, which makes it much easier for your teacher to
help you, no matter which tool you or they are using:

> **Forgot how to open Copilot Chat?** Click the chat icon at the top of the
> VS Code window, or press `Ctrl+Alt+I` (Windows/Linux) / `Ctrl+Cmd+I` (Mac).
> See `week6/deck.md` for the full setup if it's still not showing up.

> Create a Python file called weather.py that uses the requests library to talk to
> the OpenWeatherMap current weather API.
>
> At the top: `import requests` and `from config import API_KEY` — the key comes
> from config.py, do not write a real or placeholder key directly in this file.
> Also add one constant: `BASE_URL = "https://api.openweathermap.org/data/2.5/weather"`.
>
> Write a function `get_weather(city)` that:
> - Sends a GET request to BASE_URL using a `params` dict with q=city, appid=API_KEY,
>   units=metric. Do not build the URL by joining strings — use the `params` argument.
> - Checks `response.status_code` BEFORE calling `.json()`.
> - If status_code is 404, raise `ValueError(f"City '{city}' not found.")`
> - If status_code is 401, raise `RuntimeError("Invalid API key.")`
> - If status_code is anything else besides 200, raise
>   `RuntimeError(f"API error: HTTP {status_code}")`
> - Otherwise, parse the JSON and return a plain dict with exactly these keys: city,
>   country, temp, feels_like, humidity, condition, description, wind_speed. Round
>   temp and feels_like to 1 decimal place. Note that `data["weather"]` is a LIST,
>   so condition comes from `data["weather"][0]["main"]`.
>
> Write a function `get_mood(condition)` that returns one of these words based on
> the condition string: Clear→"sunny", Clouds→"cloudy", Rain or Drizzle→"rainy",
> Thunderstorm→"stormy", Snow→"snowy", Mist or Fog or Haze→"foggy", anything
> else→"unknown".
>
> At the bottom, add `if __name__ == "__main__":` that asks the user to type a city
> with `input()`, calls get_weather and get_mood, and prints each field from the
> dict on its own line, plus the mood. Wrap the call in a try/except that catches
> ValueError and RuntimeError separately, and prints the error message instead of
> crashing.

When the AI is done, open `weather.py` and check the top of the file says
`from config import API_KEY` — not a real key typed directly into the file. If
the AI wrote the key into `weather.py` anyway, delete that line and ask it to
import `API_KEY` from `config` instead.

Run it, using whichever of `python` / `python3` worked when you installed `requests`:

```bash
python weather.py
```

Type a real city. **Check both of these before moving on:**

- [ ] A real city prints all 8 fields plus the mood — no red crash text
- [ ] A fake city (try `asdkfj`) prints one clean line like `City 'asdkfj' not found.` — not a crash

**You are done with this step when both checks pass.** If your output looks a little
different from a classmate's, that's fine — different wording is normal. A crash is
not. If it crashes, go to **Section 5 — Fixing**.

---

## 4. Build the UI version — `app.py`

`weather.py` works now. Leave it alone for the rest of this project — you're only
building on top of it. If the app misbehaves from here on, the bug is almost always
in `app.py`, not `weather.py`.

Create a file called `app.py` in the same folder. Paste this prompt exactly:

> Create a Python file called app.py that builds a Tkinter window on top of
> weather.py. At the top: `import tkinter as tk` and
> `from weather import get_weather, get_mood`.
>
> Define a dictionary called MOOD_STYLES with one entry per mood: sunny, cloudy,
> rainy, stormy, snowy, foggy, unknown. Each entry is a dict with a background hex
> colour, an emoji, and a text colour. Use these exact colours:
>
> | Mood | Emoji | Background |
> |------|-------|------------|
> | sunny | ☀️ | `#FFD97D` |
> | cloudy | ☁️ | `#B0BEC5` |
> | rainy | 🌧️ | `#5C9BD6` |
> | stormy | ⛈️ | `#546E7A` |
> | snowy | ❄️ | `#E3F2FD` |
> | foggy | 🌫️ | `#CFD8DC` |
> | unknown | 🌡️ | `#ECEFF1` |
>
> Make a window, 420x520, not resizable, titled "Weather Mood App". Add, top to
> bottom: an Entry box and a Search button side by side; a large emoji Label (font
> size 80); a temperature Label (font size 42, bold); a city/country Label; a
> description Label; and an error Label with red text.
>
> When Search is clicked, or Enter is pressed in the Entry box, run a function that
> reads the city text, calls get_weather then get_mood, and on success updates
> EVERY label's text and background colour to match the mood — the window
> background AND every individual label background, not just the window. On
> ValueError, show "City not found." in the error label in red and leave the
> background unchanged. On RuntimeError, show "API error — try again." in red.
> On a successful search, clear the error label's text.
>
> Add `root.mainloop()` as the very last line — without it the window opens and
> closes instantly. Wire the button with `command=on_search`, no brackets —
> `command=on_search()` with brackets runs it immediately instead of on click.

Run it, same `python` / `python3` as before:

```bash
python app.py
```

**Check all of these before you call it done:**

- [ ] The window opens and stays open
- [ ] A real city changes the background colour and shows an emoji, temperature, and description
- [ ] No grey or white boxes appear behind any text
- [ ] A fake city shows a red error message in the window — not a crash, not a console error
- [ ] Searching a real city right after a fake one clears the red message and changes the colour again

If any of those fail, find the matching row in **Section 5 — Fixing** below.

---

## 5. Fixing things when they go wrong

Find your symptom in the left column.

| Symptom | Where it happens | Cause | Fix |
|---|---|---|---|
| `{"cod":401,...}` from curl, or `RuntimeError: Invalid API key` in Python | Step 2 or 3 | Key has a typo, or it's less than 2 hours old | Re-copy the key exactly. If it's new, wait and try again. |
| `ModuleNotFoundError: No module named 'requests'` (first time) | Step 3 | `requests` was never installed | Run `python -m pip install requests` (use `python3 -m pip install requests` if `python` isn't recognized) |
| `ModuleNotFoundError: No module named 'requests'` (even though you just installed it) | Step 3 | You installed with `python` but ran the file with `python3` (or the reverse) — pip installed it for a different Python than the one running your file | Pick one of `python` / `python3` and use that exact word for BOTH installing and running, every time |
| `command not found: python` (Mac/Linux), or `'python' is not recognized` (Windows) | Step 3 or 4 | Your computer only has `python3`, not plain `python` (common on Mac) | Use `python3` instead, for both installing and running: `python3 -m pip install requests` and `python3 weather.py` |
| `error: externally-managed-environment` when you try to pip install | Step 3 | Your computer blocks installing packages directly into its system Python (common on newer Macs) | Create a private environment just for this project: `python3 -m venv .venv`, then turn it on — Mac/Linux: `source .venv/bin/activate`, Windows: `.venv\Scripts\activate` — your prompt should now start with `(.venv)`. With it on, run `pip install requests` and `python weather.py` as normal. Turn it on again (same activate command) every time you reopen the terminal for this project. |
| `ssl.SSLCertVerificationError: ... unable to get local issuer certificate` | Step 3 | Your computer's Python doesn't yet trust the website's security certificate — common right after installing Python on a Mac | Run `pip install --upgrade certifi` (inside your `.venv` if you made one), then try again. Still failing after that? Ask your teacher — this is a one-time computer setup issue, not a mistake in your code. |
| `TypeError: list indices must be integers` | Step 3 | Code wrote `data['weather']['main']` instead of `data['weather'][0]['main']` | `weather` is a list. Add `[0]` before `['main']`. |
| A fake city crashes with `NoneType` errors later in the program | Step 3 | `get_weather` returns `None` on error instead of raising | Ask the AI: "change get_weather to raise ValueError instead of returning None" |
| The app window flashes open and closes immediately | Step 4 | Missing `root.mainloop()` | Add `root.mainloop()` as the very last line of the file |
| Clicking Search does nothing — or it ran once automatically on startup | Step 4 | `command=on_search()` has brackets | Remove the brackets: `command=on_search` |
| `ModuleNotFoundError: No module named 'weather'` | Step 4 | `app.py` and `weather.py` aren't in the same folder, or terminal is in the wrong folder | `cd` into the week7-8 folder before running `python app.py` |
| Grey or white box appears behind text when the colour changes | Step 4 | Only `root.config(bg=...)` was updated, not every Label's `bg` | Ask the AI: "make sure every Label widget's bg is also updated to match the window background" |
| The red error message never goes away, even after a real city works | Step 4 | Error label isn't cleared on a successful search | Ask the AI: "clear the error label's text at the start of a successful search" |
| Everyone's `weather.py` looks completely different | Any step | The prompt was paraphrased instead of copied exactly | Re-paste the exact prompt from this README, word for word |
| `ModuleNotFoundError: No module named 'config'` | Step 3 | `config.py` was never created, or it's named something else | Copy `config_example.py`, rename the copy to exactly `config.py`, add your key |
| `ImportError: cannot import name 'API_KEY' from 'config'` | Step 3 | `config.py` exists but doesn't have an `API_KEY =` line, or it's spelled differently | Open `config.py` and check it has exactly `API_KEY = "your_key"` |
| The AI wrote your real key directly into `weather.py` | Step 3 | The AI ignored the instruction to import from config | Delete the hardcoded key line, ask the AI to replace it with `from config import API_KEY` |

If nothing here matches, compare your file line by line against `weather.py` /
`app.py` in this folder — those are working reference versions.

---

## Reference files

`weather.py` and `app.py` in this folder are working reference implementations.
`config_example.py` shows the shape of the key file you need — copy it to
`config.py` and fill in your real key, it won't run as-is. Build your own
`weather.py`/`app.py` with the prompts above first. If something isn't matching
after trying the Fixing table, compare your version against these line by line —
don't just copy them over your own file.

---

## Save this project in its own GitHub repo

This app is yours to keep — it doesn't belong inside the shared `python102` repo.
`python102` is the class repo everyone in the course shares; pushing your project
into it would mix your files in with everyone else's. Instead, give this project
its own repo, the way you'd save a real project.

1. Go to **[github.com](https://github.com)** → click the **+** in the top right →
   **New repository**.
2. Name it something like `weather-mood-app`. Public or private, your choice.
   Check **Add a README file**. Click **Create repository**.
3. On the new repo's page, click the green **Code** button and copy the URL.
4. Open a terminal and go **outside** the `python102` folder — for example:
   ```bash
   cd ~/Desktop
   ```
5. Clone your new, empty repo:
   ```bash
   git clone PASTE_YOUR_URL_HERE
   cd weather-mood-app
   ```
6. **Before you copy anything else, protect your key.** Create a file called
   `.gitignore` in this new folder with one line inside it:
   ```
   config.py
   ```
   This tells git to never track or push `config.py`, no matter what. Do this
   now, before step 7 — not after.
7. Copy `weather.py`, `app.py`, and `config.py` from `python102/week7-8/` into
   this new `weather-mood-app` folder. Drag and drop the files in
   Finder/Explorer, or run:
   ```bash
   cp ~/code/python102/week7-8/weather.py ~/code/python102/week7-8/app.py ~/code/python102/week7-8/config.py .
   ```
   (adjust the path to wherever your `python102` folder actually is)
8. Open the new folder in VS Code: `code .` — this is now a separate project
   from `python102`.
9. **Double-check before you commit:** run `git status`. `config.py` should
   **not** appear in the list of files to be committed. If it does, your
   `.gitignore` from step 6 isn't set up right — fix that before continuing.
10. Commit and push — this pushes to *your* new repo, not `python102`, and
    your real key never leaves your computer:
    ```bash
    git add .
    git commit -m "Weather mood app"
    git push
    ```
