@echo off
for /d /r . %%D in (*) do (
    copy replace1.bat "%%D\renamer.bat"
    cd "%%D"
    call renamer.bat
    del renamer.bat
    cd..
)