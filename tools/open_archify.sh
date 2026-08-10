#!/usr/bin/env bash
set -eu

repo_root="/home/user/바탕화면/ai_os_v2"
python3 "$repo_root/tools/update_archify.py"
xdg-open "/home/user/바탕화면/ai_os_v2_archify/ai-os-v2-current-ko.html"
