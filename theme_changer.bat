@echo off
powershell -NoLogo -Command "Set-Location -LiteralPath '%~dp0'; uv run main.py"
