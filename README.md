# streaming-01-getting-started

> An opinionated way to get started with Python.

Set yourself up for productivity and collaboration.

We assume no prior programming experience and that you want to 
get productive as quickly as possible.


## Goals

- Set up a working Python environment
- Start managing data and code with GitHub and Git
- Read and execute Python code (using only the Standard Library)
- Start working with Markdown, a super simple markup language 
- Explore a variety of data and code


## Task 1. Sign Up for GitHub (free)

Sign up for a free account with [GitHub](https://github.com/), a code hosting platform that manages a vast number of programming projects. 
Follow their website instructions to get started. 
See the recommendations on GitHub email and username below.

### GitHub Email 

You'll need an email. 
I use a permanent personal email for most GitHub work, rather than a work or school account (which may be temporary).
Your email will not be made public.

### GitHub Username

You'll create a GitHub username. 
Your username will be public.
Your username can be anonomyous (e.g., 'analystextraordinaire') or publicly associated with you. For example, I use 'denisecase'.
Your username will be a part of the URL to all of your projets. 

Q: Find the username in this repo URL:

<https://github.com/denisecase/datafun-00-getting-started>

Recruiters may look at GitHub and LinkedIn profiles - it can be helpful to show your skills using modern tools. 
Be courageous. The best way to learn is by doing, and
don't be too concerned about making mistakes. 
Mistakes are common getting started, 
and learning to fix issues is a key skill in data analytics. 
Keep and share your latest, most useful, and best work.

## GitHub Repositories

Each coding project lives in a GitHub repository (called 'repo' for short) in the 'cloud' (a distributed group of machines).

- Git (the system) keeps track of committed changes to an evolving project. 
- The GitHub repo can be kept in sync with a git repo on your local machine. 
- For example:
    - This GitHub repo is named **streaming-01-getting-started**. 
    - On my machine, it's in my **Documents/streaming-01-getting-started** directory.

For more about GitHub and repos, see [Skills-GitHub](docs/Skills-GitHub.md).

Q: When viewing this GitHub repo in your browser, can you find the username and repo name in the URL? 

Once you have a GitHub account, continue.


## Installations

You'll need the following tools installed on your local machine:

1. **Git** - code management and version control system that interacts with GitHub
1. **Python (Version 3.11 or greater)** -  popular, powerfull scripting programming language
1. **VS Code** - lightweight, cross-platform editor that helps with code completion, code formatting, and more.
1. **VS Code Extension: Python (by Microsoft)** - makes VS Code fun for Python
1. **VS Code Extension: GitHub (by GitHub)** - makes Git fun with VS Code

See the following subsections for installation recommendations. 

## Explore!

When installing, following instructions is necessary, but not sufficient.

Try to understand every new tool installed, accessed, or joined. 

While downloading, 

- Review the web site.
- Read the 'Introduction and 'Getting Started' sections.
- Do a quick search to see:
    - who uses it, 
    - what it offers, 
    - why it's popular, and 
    - when and how it's used.

_Important: Follow instructions carefully when installing and configuring a tool._ 
_Computers are notoriously pedantic._
_Capitalization, spelling - even tabs and spaces - matter a lot!_

In general, after installing and configuring any new tool:

- Verify the installation by checking the version.
- Start it.
- Click and explore the menus, tabs, icons. Try to get an overview of what is possible and how things are arranged. 
- Hovering the mouse over an icon in VS Code will provide a 'tooltip' with more information.

## Task 2. - Install Git

If you don't already have Git, follow the instructions. 
If you think you might, try checking the version as shown below.

Install - and setup - your Git installation using this guide: <https://github.com/git-guides/install-git>.
Do not install GitHub Desktop. 
We will use other tools to manage git. 
Skip the GitHub Desktop part and go down to the instructions for your operating system. 

Verify installation by checking the version. Open a new Terminal (macOS) or PowerShell (Windows/macOS) and type the following, then hit return/enter:

`git version`


## Task 3. - Install Miniconda3

If you don't already have Python, follow these instructions. 

Existing users: 

- We use conda rather than pip. It makes some aspects of Python nicer.
- If you **can** change your Python installation (or add a new one), do so.
- If you **cannot** chanage your Python installation, e.g., work requires 3.6 and pip, some features **will not work** as expected. As we add features, work with the people responsible for your Python environment. 

Install Python 3 using the **Miniconda3** distribution by following the instructions at this link:<https://docs.conda.io/en/latest/miniconda.html>.

Read and follow their installation guidelines for your operating system and machine (most will be 64-bit). Note:

_"On Windows, macOS, and Linux, it is best to install Miniconda **for the local user**, which does not require administrator permissions and is the most robust type of installation."._ 

**Miniconda3** includes Python and **conda** (an important tool for managing Python packages and environments). 
More information is available below.

Verify installation. Open a new Terminal (macOS) or open Anaconda Prompt (Windows) and type the following, then hit return/enter:

`conda update conda`

Then again, type the following and hit return/enter:

`python --version`

Then try each of these commands (hit enter after each - we won't usually repeat that part):

```
conda list
python
```

Q: Do you see >>>? 

That means you're in interactive Python mode. 
You can now run Python commands. 

Type `2+2` and hit return/enter. Python handles expressions.

Type `print("Hello, world!")` and hit return/enter. You just called the builtin print() function.

Do a web search for "how to exit interactive Python mode" to get out - or call the builtin exit() function (like you did print() above).

Congratulations - that's a great start - being able to execute Python commands makes amazing things possible! 

## Task 4. - Install VS Code Editor

Install the **VS Code** editor from here: <https://code.visualstudio.com/download>.

If you need more help, use the official VS Code docs, for example, 
additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).

_Recommendation: Add VS Code to your Dock (macOS) or Start Menu (Windows)._

After installing, open VS Code. 
Explore the information provided - check out the menus. 

_Recommendation: In VS Code, verify File / Autosave is checked._  

## Task 5. - Install VS Code Extension: Python

After VS Code installs, install the VS Code Python extension from here: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.

If you have troubles installing, click the link that says "Trouble Installing?" and it will show you how to add extensions from within VS Code.

Once you install the extension, it'll ask if you want to get started with Jupyter Notebooks.
Ignore this for now - close that tab in VS Code.

## Task 6. - Install VS Code Extension: GitHub Repositories

In VS Code, look at the icons down the left. Look for 4 squares.
Mouse over it to see the tooltip "Extensions". Click it. 

On the top of the primary left side panel, you'll see the installed extensions. 

If **GitHub Repositories** is not installed, find it in the recommended list of extensions below, do a web search, or find it here: <https://marketplace.visualstudio.com/items?itemName=github.remotehub>


## After Installs 

_Recommendation: After doing any major installation, restart VS Code, restart your terminal, and sometimes, restart your machine before continuing. Ensure your environments are fully updated._

:white-check-mark: Adding extensions to VS Code is a generally useful skill.


## Task 7. Fork this Repo 

Your machine is ready. Now let's get some code. 

First, we'll get this repo into **your** GitHub account. 

1. Open your browser to <https://github.com/denisecase/streaming-01-getting-started>.
1. Look at the URL and the web page - note the account is denisecase.
1. Look at all the options available for a repo. 
1. Find and click the Fork button at the top.
1. Keep the defaults and click 'Create Fork'. 
1. When it finishes, look at the repo - note the account.

Forking is just a term for copying a repo from one account to another.

## Task 8. Clone Your Repo

Now we want to clone your new GitHub repo down to the Documents folder on your local machine. 

1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it.
1. Provide the URL of **your** new GitHub repo.
1. When it asks where to put it, select your Documents folder.

Note: The first time you do this, you'll be guided through a process to sign into GitHub from VS Code. 

You can read more about cloning - and clone your repo without VS Code by following the instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

When complete, you'll have a new folder in your Documents directory:

`Documents/streaming-01-getting-started`

## Task 9. Explore Repo in VS Code

Explore your new project repo in VS Code. 

If the project is not already open in VS Code:

1. Open VS Code.
1. From the menu choose File / Open Folder / and select Documents/streaming-01-getting-started.
1. In the primary side bar, expand the repo folder. 

Once opened, explore - consider these questions:

1. Where is this README.md file? 
1. Can you see a .gitignore file? 
1. What do you think the .gitignore file does? (Hint: open it.)
1. Can you find a Python script file (.py)?
1. Click on the file to open it in the editor.
1. Can you figure out how to run the file?


## Task 10. Execute Python Scripts

1. Click on the about.py file to open it for editing.
1. Click the run button (arrow) in the upper right to execute.
1. If successful, you should get a new about.txt file. 

For more information about options for executing a Python program in VS Code, see [Run Hello World](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

About.py provides a lot of useful information about your Python environment. 
Review these paths carefully - it tells alot about your Python installation and environment. 

Open, read, and run each of the remaining files in order. 
You don't need to understand the code yet. 

Instead, try to figure out what each file is doing. 
Like learning any new language, reading is bit easier than 
writing - we can learn much just by seeing it. 

By the end of the course, the code will make much more sense. 

## Task 11. Check the Boxes

Next, edit this Markdown file to record how things went.

1. In the checklist below, mark the tasks completed that you were able to complete successfully. 
1. If any could not be completed, leave them as they are.  


## Task 12. Commit Changes and Push to GitHub

1. On the VS Code side panel, click the source control icon (has blue bubble with an number in it).
1. Important! Above the blue Commit button, it will say "Message". You must include a message. 
1. In that message input box, type "getting set up".
1. Click the blue "Commit" button and follow instructions to Commit your code. and push it up to your GitHub repo. 

Open a browser to your GitHub repo and see if the files have appeared. 

In additon to about.txt, you should have additional data files as well. 

If not return to VS Code and execute the files until you have generated celcius and kelvin csv files.

If your computer hangs because you forgot a commit message, 
just enter your message in the top line of the file it shows in the editor.
Then click the checkmark in the upper right to close that file and save your commit message.


## Checklist

Change the open boxes [ ] below to checked boxes [x] as you complete the tasks.

- [ ] Task 1. Sign up for GitHub
- [ ] Task 2. Install (and configure) Git
- [ ] Task 3. Install Miniconda3
- [ ] Task 4. Install VS Code
- [ ] Task 5. Install VS Code Extension: Python
- [ ] Task 6. Install VS Code Extension: GitHub Repositories
- [ ] Task 7. Fork this repo into your account
- [ ] Task 8. Clone your new GitHub repo down
- [ ] Task 9. Explore the repo in VS Code
- [ ] Task 10. Execute a Python script.
- [ ] Task 11. Check the boxes (edit a Markdown file)
- [ ] Task 12. Commit changes (with a message!) and push to GitHub


## Computer View Settings

Update the important view settings as needed.

## View File Extensions

When negotiating files and folders, you should be able to view file extensions (e.g, .py, .md). 
If these aren't visible, seach for how to view file extensions on your operating system. 

## See Hidden Files

You may want to see hidden files. 
Find this option in the Windows File Explorer ribbon.
Toggle it in Mac Finder with Command Shift dot.

Your repo has a hidden .git folder that maintains changes to your code.
Do a web search to learn more as needed.


## Resources

1. For more information about Git in VS Code, see [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview.

1. For more information about editing Markdown task lists, see [how to mark a task complete](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists).

1. For more information about editing Markdown in VS Code, see [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown).