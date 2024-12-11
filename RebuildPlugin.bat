@echo off
setlocal enabledelayedexpansion
:: Get the plugin directory from the batch file location
set "PLUGIN_DIR=%~dp0"
:: Get parent folder name by removing trailing backslash and getting last folder name
set "PLUGIN_DIR_NOSLASH=%PLUGIN_DIR:~0,-1%"
for %%I in ("%PLUGIN_DIR_NOSLASH%") do set "PLUGIN_NAME=%%~nxI"

:: Find the .uplugin file
for %%F in ("%PLUGIN_DIR%\*.uplugin") do (
    set "UPLUGIN_FILE=%%F"
)
if not defined UPLUGIN_FILE (
    echo Error: No .uplugin file found in directory.
    pause
    exit /b 1
)

:: Hardcoded engine paths. They can be the same if the source code isn't dependant on a specific engine version.
set "FROM_ENGINE=C:\Program Files\Epic Games\UE_5.0"
set "TO_ENGINE=C:\Program Files\Epic Games\UE_5.0"

:: Create temp build directory with plugin name
set "TEMP_BUILD_PATH=%USERPROFILE%\Desktop\PluginBuild\%PLUGIN_NAME%"
if exist "%TEMP_BUILD_PATH%" (
    rmdir /s /q "%TEMP_BUILD_PATH%"
)
mkdir "%TEMP_BUILD_PATH%"

echo.
echo Building plugin %PLUGIN_NAME%...
echo From: %UPLUGIN_FILE%
echo To: %TEMP_BUILD_PATH%
echo.

:: Run the build command in a separate process and wait for it
call "%TO_ENGINE%\Engine\Build\BatchFiles\RunUAT.bat" BuildPlugin -plugin="%UPLUGIN_FILE%" -package="%TEMP_BUILD_PATH%" -TargetPlatforms=Win64

:: Store the error level immediately
set BUILD_RESULT=%ERRORLEVEL%

:: Check if build was successful
if %BUILD_RESULT% NEQ 0 (
    echo.
    echo Build failed!
    pause
    exit /b 1
)

:: Ask if user wants to install to another project
echo.
echo Build successful! Would you like to install this plugin to another project? (Y/N)
set /p INSTALL_CHOICE="Choice: "

if /i "%INSTALL_CHOICE%"=="Y" (
    set /p PROJECT_PATH="Enter project path: "
    if not exist "!PROJECT_PATH!\Plugins" mkdir "!PROJECT_PATH!\Plugins"
    if exist "!PROJECT_PATH!\Plugins\%PLUGIN_NAME%" (
        echo.
        echo Warning: Plugin already exists in project. Delete existing? (Y/N)
        set /p DELETE_EXISTING="Choice: "
        if /i "!DELETE_EXISTING!"=="Y" (
            rmdir /s /q "!PROJECT_PATH!\Plugins\%PLUGIN_NAME%"
        ) else (
            echo Installation cancelled.
            pause
            exit /b 0
        )
    )
    xcopy /s /e /i /y "%TEMP_BUILD_PATH%" "!PROJECT_PATH!\Plugins\%PLUGIN_NAME%"
    echo Installed to project plugins directory.
) else (
    echo Plugin remains in: %TEMP_BUILD_PATH%
)

echo.
echo Process complete!
pause
