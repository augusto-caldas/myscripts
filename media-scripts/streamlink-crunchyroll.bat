@echo off

set mpvPath=""

set crunchyrollUsername=""
set crunchyrollPassword=""

:replay

set /p videourl="URL: "

streamlink --crunchyroll-username="%crunchyrollUsername%" --crunchyroll-password="%crunchyrollPassword%" "%videourl%" best --player "%mpvPath%"

goto replay