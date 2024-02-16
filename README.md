# Open Link in Chrome

Firefox extension that adds context menu option (right click on link) to open links in Chrome browser.


## How does it work? and why do I need an external program?

Firefox extensions can't open/access other browsers, so we need to use something which allow us to do it. That thing is Native Messasing which allows extension and Native Messaging Host to communicate who can open other browsers. The executable file you see in [releases][1] for your OS is that Native Messaging Host.

## Installation

- Install extension from https://addons.mozilla.org

__Note__: If you don't trust the executable files provided in [releases][1], then you can generate your own excutables. See [here](#generate-your-own-excutable-files) how to do it.

### Ubuntu

- From __Ubuntu__ [releases][1] download `open_link_in_chrome_host.json` and `open_link_in_chrome_host`

- Move `open_link_in_chrome_host` anywhere you want, where you will not accidently delete it

- Edit "path" value in `open_link_in_chrome_host.json` and put exact path of `open_link_in_chrome_host`

- Move `open_link_in_chrome_host.json` to `/home/<your_username>/.mozilla/native-messaging-hosts/`

### Windows

- From __Windows__ [releases][1] download `open_link_in_chrome_host.json` and `open_link_in_chrome_host.exe`

- Move both files anywhere you want where you will not accidently delete them

- Edit "path" value in `open_link_in_chrome_host.json` and put exact path of `open_link_in_chrome_host.exe`

- Add Registry key by executing following commands in __Powershell__,  Replace `<path to open_link_in_chrome_host.json>` with exact path of `open_link_in_chrome_host.json`

    ```
    New-Item -Path "HKLM:\SOFTWARE\Mozilla\NativeMessagingHosts\open_link_in_chrome_host" -Force | Out-Null

    New-ItemProperty -Path "HKLM:\SOFTWARE\Mozilla\NativeMessagingHosts\open_link_in_chrome_host" -Name "(Default)" -Value "<path to open_link_in_chrome_host.json>" -PropertyType String -Force
    ```

---

## Development related stuff

### Load temporary extension

- Open `about:debugging#/runtime/this-firefox` and select manifest.json file

### Generate your own excutable files

> You are on Ubuntu and have Python installed, then consider this:
>
> If you have Python installed and using Ubuntu you don't need to do this. In `./Native-Messaging-Host/Ubuntu` folder open_link_in_chrome_host.py has shebang notation (first line), just put appropriate name on that line `python` or `python3` based on how you access python in your system and use that file in place of executable file (in installation where I have mentioned `open_link_in_chrome_host` just consider `open_link_in_chrome_host.py`, make sure to do the same in .json file "path" value)

__Note__: If you follow below steps in Windows, then generated file can only be used in Windows. If you follow below steps in Ubuntu, then generated file can only be used in Ubuntu.

- Install Python module `Pyinstaller` (I prefre this module)
    `python3 -m pip install pyinstaller`
- Open terminal and go to (replace <Your_OS> with Windows or Ubuntu)
    `./Native-Messaging-Host/<Your_OS>/open_link_in_chrome_host.py`
- Run command `python3 -m pyinstaller open_link_in_chrome_host.py --onefile`
- Generated file will be in `./Native-Messaging-Host/<Your_OS>/dist/`
- Take that file instead of one provided in [releases][1] for your OS, and follow [Installation instructions](#installation)





[1]: https://github.com/rajan-31/open-link-in-chrome/releases