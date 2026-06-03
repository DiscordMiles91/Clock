import PyInstaller.__main__

PyInstaller.__main__.run([
    'clock.py',
    '--name=Clock',
    '--distpath=dist',  
    '--add-data=clock.ico;.', 
    '--clean',
    '--onefile',
    '--windowed',
    '--noconsole',
    '--icon=clock.ico',
], )