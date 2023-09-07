![ICON](icon.svg)

# Impaler Launcher
A Python Qt5 Minecraft Launcher with instances

With offline play and Ely By authenticated accounts (No Mojang nor Microsoft)

Support for Vanilla and Fabric versions (No Forge)

Programed by [@sir-vladimir](https://github.com/sir-vladimir) (Me) and UI by [@scriniariii](https://github.com/scriniariii)

(Sir Vladimir Productions)

## Run

Tested with Python `3.11.5`

Clone repository and make a virtual environment with requirements then run (Linux) (Bash)

```
git clone https://github.com/sir-vladimir/impaler_launcher.git
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```
Now login into your Ely By account or use offline mode

Then create a named instance with desired version and optional Fabric checkbox

Java path is optional and selects default installed version, be sure to install a JRE or JDK first

Set memory usage or others in JVM arguments, can be later changed in configure instance

Now it will install Minecraft to `HOME/.impaler/minecraft/` and instance to `HOME/.impaler/instances/NAME` and finally launch the instance

## Compile

Use `pyinstaller -Fw -i icon.ico main.py` to make an executable for your running platform with `pyinstaller` package
