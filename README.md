# -CatchStealer-

<p align="center">
    <br /><br />
    <img alt="Language: Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <p>A Python 🍪 stealer with e-mail logging</p>
</p>

CatchStealer can steal cookies/other info(Screenshot, OS, TIME, Username) and send logs to your e-mail

# Features of CatchStealer

  - Builder with custom config
  - E-Mail logging
  - Automatically compiling to .exe file
  - Using .zip file for logging
  - More functionally


# Supported browsers
 Here you can see list of supported/unsupported browsers
| Browser | Support status |
| ------ | ------ |
| Google Chrome | True |
| Opera | True |
| Yandex browser | True |
| Firefox | True |
| IE | False, because it dead |
| Edge | False, impossible to steal |

### Prepare to building

* Clone that repository
* Install all dependencies for pip

```sh
$ pip3 install -r requirements.txt
```

* Configure the builderconf.yml file. Example of right config:
> pyconf:
    pipExec: pip3
> builder:
    stealerlogging: False 
    mail:  example@gmail.com
    mailpassword: password
    execompile: True 
    getotherlog: True 
    logfilename: log.zip 
    removelog: True 

Also you can check comments, it may help you for build.

* Run builder.py

And just wait until your build will be builded.

### Exceptions of builder:

If configuration file have some problems, builder will show it. Here is exception list:

| Exception | Description |
| ------ | ------ |
| COULDN'T LOAD CONFIG(builderconf.yml) | It means builder cannot find builderconf.yml, copy your configuration file to builder directory and try again. |
| FAILED TO LOAD CONFIG FILE. PROBLEM WITH SYNTAX | It means your configuration file have problem with syntax. Download config again and configure it. |
| INCORRECT E-MAIL ADDRESS! ONLY GMAIL SUPPORTED!!! | Just change your e-mail from configuration. Only GMail support. |
| NO PASSWORD! | You forgot to insert password :) |
| FAILED TO LOAD SOURCE FILE, WAITING | It means builder cannot find source file(main.py) Clone repository again and try it.|


### Q:A

* Why builder needs my e-mail password?
> Because your logs will be send to your e-mail.

* I'm not getting logs
> Probably, your credentials (e-mail; password) is invalid. Re-build it and try again.

* I'm getting pip exception while building
> Maybe you insert incorrect pip command in configuration file. Try pip; pip3

* Antivirus detect my stealer. What i should do?
> Try to crypt your exe file

### Modify source code?
Yes, you allowed to edit source file.

### Example of logging:

![Example of logging](https://i.imgur.com/0q5LoYa.png)

##### Developed by CatchThels ~ 2020
