@echo off
rem FileNameRandomizer v1.0.1.
rem Randomize file names in the specified directory using optional file mask.
rem https://pastebin.com/u/jcunews
rem https://www.reddit.com/user/jcunews1/

setlocal enabledelayedexpansion
if "%~1" == "" (
  echo Usage: FileNameRandomizer {directory} [file mask]
  echo.
  echo Examples:
  echo   FileNameRandomizer "e:\data\test files"
  echo   FileNameRandomizer ..\testdir *.txt
  echo   FileNameRandomizer testdir "the file*.*"
  goto :eof
)
pushd %1
if errorlevel 1 goto :eof
set mask=%~2
if "%mask%" == "" set mask=*

rem *** get file list
echo Retrieving file list...
set namecount=0
for %%A in (%mask%) do (
  set/a namecount+=1
  set name!namecount!=%%A
)
if %namecount% == 0 (
  echo No file found.
  goto :eof
)

rem *** generate random file list
echo Generating randomized file list...
:mkrnd
for /l %%A in (1,1,%namecount%) do (
  set tmp%%A=!name%%A!
  set rnd%%A=
)
set i=1
:getrnd
set/a r=%random%%%namecount+1
if %r% == %i% (
  rem *** restart list randomizer if last item end up having itself to choose
  if %r% == %namecount% goto mkrnd
  goto getrnd
)
if "!tmp%r%!" == "" goto getrnd
set rnd%i%=!tmp%r%!
set tmp%r%=
set/a i+=1
if %i% leq %namecount% goto getrnd

rem *** rename files to random names
echo Renaming files...
for /l %%A in (1,1,%namecount%) do (
  set tmp%%A=file%%A.tmp
  ren "!name%%A!" !tmp%%A!
)
for /l %%A in (1,1,%namecount%) do (
  echo !name%%A! ^>^> !rnd%%A!
  ren !tmp%%A! "!rnd%%A!"
)