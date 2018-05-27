@echo off
Setlocal enabledelayedexpansion

Set "Pattern=- Replace This"
Set "Replace=- With This"

For %%# in (*.ext) Do (
    Set "File=%%~nx#"
    Ren "%%#" "!File:%Pattern%=%Replace%!"
)
