@shift /0
SetLocal EnableDelayedExpansion

@echo off
TITLE Just Dance Wii Texture Tools by Yunyl
mode con: cols=84 lines=32
color AF

goto :HideMenu



:HideMenu
color 0D
cls
echo.
echo   Welcome to Just Dance Wii Texture Tools by Yunyl (1.0.5)
colorecho " Encode Wii Texture" 14
echo     [1] Convert 256x512 folder to SSD
echo     [2] Convert AlbumBKG or square
echo.
echo [3] Exit
echo.
set /p opt=Type option and press Enter:
if "%opt%"=="1" ( 
cls
echo.
echo  Finding the textures...
python "%~dp0mask_256x512.py" %1
python "%~dp0encode_folder_256x512.py" %1 "OUTPUT_256x512"
del OUTPUT_256x512\*.bti
del OUTPUT_256x512\*.png
goto :HideMenu
)
if "%opt%"=="2" ( 
cls
echo.
echo  Finding the textures...
python "%~dp0encode_folder_albumbkg.py" %1 "INPUT_ALBUMBKG"
del INPUT_ALBUMBKG\*.bti
del INPUT_ALBUMBKG\*.png
goto :HideMenu
)
EndLocal