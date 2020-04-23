# <img src="https://www.countryflags.io/gb/shiny/48.png" alt="Logo" height="24"> Covid-19 United Kingdom Tracker

[About the Project](#about-the-project) | [How to Install](#how-to-install) | [Set up my own tracker](#set-up-my-own-tracker) | [License](#license)


## About The Project

[Bitbar](https://getbitbar.com/) Plugin to track Covid-19 cases in the United Kingdom from the MacOS menu bar.

**Built with:**

- [Bitbar](https://getbitbar.com/)
- [Novel COVID API](https://github.com/NovelCOVID/API)

![](https://github.com/bryandms/covid-19costaricatracker/blob/master/media/minimisedpreview.png?raw=true)

![](https://github.com/bryandms/covid-19costaricatracker/blob/master/media/fullscreenpreview.png?raw=true)

## How to Install

**1. Installing BitBar**

There are two ways to install BitBar on your Mac:

- Use Homebrew: `brew cask install bitbar`.
- Or download .app file directly: [Get the latest version of BitBar](https://github.com/matryer/bitbar/releases). Then copy it to your Applications folder and run it - it will ask you to (create and) select a plugins folder, do so.

**2. Installing Python**

- Install Python by following the [instructions here](https://www.python.org/downloads/).
- Make sure your node exec resides in `usr/local/bin/node`, else you will have to update the path in the script.

**3. Installing requests with pip**

- Run `sudo -H pip install requests --upgrade` to install the latest version of the requests module

**4. Saving this script**

- Download the [script](https://github.com/benjamin-sommer/covid-19-uk-tracker/master/covid-19-uk-tracker.py) on your local machine. Make sure you place this file in the same plugin folder which you created while installing Bitbar.
- Go to the plugin folder and run `chmod +x covid-19-uk-tracker.py`
- Refresh Bitbar.

## License

[See license](https://github.com/benjamin-sommer/covid-19-uk-tracker/master/LICENSE)
