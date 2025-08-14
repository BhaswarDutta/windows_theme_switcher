@echo off
powershell -NoExit -Command "Set-Location -LiteralPath '%~dp0'; uv run main.py"
