# P5: Frontend

**Assigned**: Oct 21

**Due**: Nov 8, 11:59 PM

**Late Deadline**: Nov 11, 11:59 PM

## Description

Improve Project 2 by adding styles and interactivity to the website.

## Setup

Activate your venv, navigate to `p5/` and run `pip3 install -r requirements.txt`.\
Alternatively: `pip3 install Flask requests python-dotenv`.

To use Tailwind locally (which enables intellisence), you will need to [download Node.js](https://nodejs.org/en/download/).

> [!CAUTION]
> On WSL, **do not run** `sudo apt-get update` and `sudo apt install nodejs` as that will install an old outdated version of node.js. Instead, use [nvm](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl).

> [!TIP]
> I recommend setting up [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating) even if you are on Linux on Mac, it makes it easier to manage Node versions. Simply run `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`, and then you should be able to run `nvm install 20` (version 20 is the latest LTS version of Node.js), and then `nvm use 20` (it's sort of like enabling your venv for python, when you run `npm install` commands later, it's sort of like running `pip install` for your flask packages). For troubleshooting, see the [docs](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

## Project

### Part 1: Styling

#### Setup:

For Tailwind, you can either use the [Play CDN](https://tailwindcss.com/docs/installation/play-cdn) or install [Tailwind CLI](https://tailwindcss.com/docs/installation).

To use the **CDN**, no setup is needed, just put the CDN `<link>` in your `base.html` inside the `<head></head>` tag.

For **Tailwind CLI** the correct `tailwind.config.js` has already been provided, run the provided `./tw.sh` to generate a "compiled" `output.css` file (which is already linked in your `base.html` for you).

> [!NOTE]
> Before running `./tw.sh`, you might need to run `chmod +x tw.sh` in the terminal.
> To exit the Tailwind compiler, press `Ctrl + C` in the terminal.

To see your styles update in real time as you're editing them, update your flask version by running `pip install --upgrade flask`
and then run `flask run --debug` in parallel with `./tw.sh` in the terminal (you can use separate terminal tabs for this).

[^1]: The `--debug` flag will allow you to see any styling changes you've made by simply refreshing the page, but without restarting the Flask server.

> [!NOTE]
> Make sure you are running both the provided `./tw.sh` script the flask server in `--debug` mode at the same time.

> [!TIP]
> you can install a VSCode extension for [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) to get suggestions for Tailwind classes as you type them out.
> ![](image.png)

#### Requirements:

Your goal for _Part1_ is to rewrite 3 existing CSS files (`base.css`, `poke-grid.css`, and `poke-info.css`) using Tailwind utility classes.

- Open each template file side by side with respective CSS file (`poke-grid` is for `index.html`, the rest are named the same as the template file that uses them) and start replacing `TODO`s with classnames (they can get pretty lengthy, that is okay).
- As you progress, you can comment out the CSS styles one by one as you add Tailwind classes for them, in the end the website should look the same as it was when you started.
- Don't worry too much about getting the `px` or `rem` values to match exactly, avoid using `-[custom values]` in brackets as much as possible, get them close enough with Tailwind defaults (`1` = `4px` = `0.25rem`, `4` = `16px` = `1rem`, see [full table](https://tailwindcss.com/docs/margin) for sizing reference).

> [!IMPORTANT]
> Extra Credit: there are 5 extra credit styles for 10 bonus points that can cover any missing points from the 60 points available for this part.

Once you're done, comment out or remove the 3 stylesheet links in your `base.html` below the `<!-- TODO: comment these out -->` line.

> [!TIP]
> - for `@media (min-width:)` queries, see [https://tailwindcss.com/docs/screens](https://tailwindcss.com/docs/screens) for the right breakpoint prefixes (`sm:`, `md:`).
> - for `@media (max-width:)` it's in reverse. tailwind is mobile-first, meaning mobile styles are default (the stuff inside your max-width media query), and you add prefixes for larger screens (the stuff outside the media query).
> - for `@media (prefers-color-scheme: dark)` styles, use the `dark:` prefix (see [https://tailwindcss.com/docs/dark-mode](https://tailwindcss.com/docs/dark-mode)).

### Part 2: Interactivity

For this part, you need to complete the search functionality by filling out the `<script>` tag in `base.html`.

The search functionality should filter the list of Pokemon by name as the user types in the search bar.

- First, get an element by id `"#search"` (the input field located in `macros/search.html`).
- Next, get an array of all link (`<a>`) elements.
- Add an event listener to the input field that listens for the `"input"` event.
  - When the event is triggered, get the search value from `e.target.value` and convert it `toLowerCase()`.
  - Then, _for each_ of the links, check if `link.textContent` converted `toLowerCase()` matches your search value.
  - If it does, set `link.style.display` to `"flex"`, otherwise set it to `"none"`.

> [!NOTE]
> We've used a macro for the search bar for this project, you only need to write the script once in `base.html`, and the searchbar will be available and working on both the index (`/`) page and the ability page.

## Submissions

Take screenshots of the finished index (`/`) page and one of the poke_info pages (`/pokemon/<id>`) and add them to your repo.
Make sure to comment out the 3 stylesheet links in your `base.html` below the `<!-- TODO: comment these out -->` line.

We'll be using Github Classroom for this project.

> [!IMPORTANT]
> Log into your Gradescope account and go to your account settings. Scroll down to the `Linked Accounts` section. If you do not already
> have your GitHub account linked here, click the `Link a GitHub account` button and log into your GitHub account.

Whenever you want to submit your project to Gradescope, you will need to push your latest version to your repo. Follow these steps to do so:

First, make sure all your changes are pushed to GitHub using the git add, git commit, and git push commands.

Next, to submit your project, you can run `submit` from your project directory.

> [!NOTE]
> you will need to have `opam` package `gradescope-submit` installed. If you don't have it on your system from 330, you can use the UI on Gradescope to link your Github repository.

The submit command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to Gradescope.

## Grading

| Requirement                                                                        | Points |
| ---------------------------------------------------------------------------------- | ------ |
| Tailwind (1 point for each missing css line to utility class conversion, total 60) | 60     |
| JavaScript (the search should be working on both the index and ability pages)      | 40     |

The project will be graded out of a 100 points.
