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

**Keep your key private.** Don't post it in chat, don't screenshot it, don't commit it
to a public GitHub repo (more on this in step 5).

---

## 2. Test the key with `curl`

Open the terminal in VS Code — the same terminal you've used all course.

Paste this, replacing `YOUR_KEY_HERE` with your real key:

```bash
curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY_HERE&units=metric"
```

**What success looks like:** one long line of text starting with `{"coord":` and
containing `"main":{"temp":` somewhere in the middle, with a real number after `temp`.

If you see that — your key works. Go to step 3.

If you see something else, use this table before touching any Python:

| You see | What it means | What to do |
|---|---|---|
| `{"cod":401,"message":"Invalid API key..."}` | Key is wrong, or not active yet | Re-copy the key exactly — no extra spaces, no quotes included by accident. If the key is less than 2 hours old, wait and try again. |
| `{"cod":"404","message":"city not found"}` | Your key **works** — the city name is the problem | Not a key issue. Try `q=Toronto` or another real city. |
| `curl: command not found` | Rare — usually an old Windows setup | Make sure you're using the VS Code terminal, not a separate Command Prompt. Ask your teacher if it persists. |
| Nothing happens, it just hangs | No internet, or the network is blocking the request | Ask your teacher — this is a network problem, not a code problem. |

Do not open your AI tool and start prompting it until `curl` shows you real weather
data with a `temp` in it. If `curl` doesn't work, your Python won't either, and
you'll waste time thinking your code is broken when it's actually the key.

---

## 3. Build the CLI version — `weather.py`

Your key works now, so the rest of this is just code.

Create an empty file called `weather.py` in this folder — don't type anything into
it yet. The prompt below creates the whole file for you, including a placeholder
line for your key. If you paste your real key in first and then run the prompt,
the AI will overwrite the file and your key will be gone again.

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
> At the top: `import requests`, then two constants: `API_KEY = "YOUR_API_KEY_HERE"`
> and `BASE_URL = "https://api.openweathermap.org/data/2.5/weather"`.
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

When the AI is done, open `weather.py` and find this line near the top:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

Replace `YOUR_API_KEY_HERE` with your real key, keeping the quotes:

```python
API_KEY = "paste_your_real_key_here"
```

This is the only line you should ever hand-edit in this file. If you ask the AI
for more changes later and it regenerates the whole file, check this line didn't
get reset back to the placeholder.

Run it:

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

Run it:

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
| `ModuleNotFoundError: No module named 'requests'` | Step 3 | `requests` isn't installed | Run `pip install requests` in the terminal |
| `TypeError: list indices must be integers` | Step 3 | Code wrote `data['weather']['main']` instead of `data['weather'][0]['main']` | `weather` is a list. Add `[0]` before `['main']`. |
| A fake city crashes with `NoneType` errors later in the program | Step 3 | `get_weather` returns `None` on error instead of raising | Ask the AI: "change get_weather to raise ValueError instead of returning None" |
| The app window flashes open and closes immediately | Step 4 | Missing `root.mainloop()` | Add `root.mainloop()` as the very last line of the file |
| Clicking Search does nothing — or it ran once automatically on startup | Step 4 | `command=on_search()` has brackets | Remove the brackets: `command=on_search` |
| `ModuleNotFoundError: No module named 'weather'` | Step 4 | `app.py` and `weather.py` aren't in the same folder, or terminal is in the wrong folder | `cd` into the week7-8 folder before running `python app.py` |
| Grey or white box appears behind text when the colour changes | Step 4 | Only `root.config(bg=...)` was updated, not every Label's `bg` | Ask the AI: "make sure every Label widget's bg is also updated to match the window background" |
| The red error message never goes away, even after a real city works | Step 4 | Error label isn't cleared on a successful search | Ask the AI: "clear the error label's text at the start of a successful search" |
| Everyone's `weather.py` looks completely different | Any step | The prompt was paraphrased instead of copied exactly | Re-paste the exact prompt from this README, word for word |
| `RuntimeError: Invalid API key` after it worked before | Step 3 | A new AI prompt regenerated the whole file and reset `API_KEY` back to `"YOUR_API_KEY_HERE"` | Open `weather.py` and paste your real key back into the `API_KEY` line |

If nothing here matches, compare your file line by line against `weather.py` /
`app.py` in this folder — those are working reference versions.

---

## Reference files

`weather.py` and `app.py` in this folder are working reference implementations.
Build your own with the prompts above first. If something isn't matching after
trying the Fixing table, compare your version against these line by line — don't
just copy them over your own file.

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
6. Copy `weather.py` and `app.py` from `python102/week7-8/` into this new
   `weather-mood-app` folder. Drag and drop the files in Finder/Explorer, or run:
   ```bash
   cp ~/code/python102/week7-8/weather.py ~/code/python102/week7-8/app.py .
   ```
   (adjust the path to wherever your `python102` folder actually is)
7. Open the new folder in VS Code: `code .` — this is now a separate project
   from `python102`.
8. **Before you commit:** open `weather.py` and check your real API key isn't
   about to go public. If this repo is or might become public, replace your real
   key with `"YOUR_API_KEY_HERE"` before committing — you can always paste the
   real one back in locally when you want to run it.
9. Commit and push — this pushes to *your* new repo, not `python102`:
   ```bash
   git add .
   git commit -m "Weather mood app"
   git push
   ```
