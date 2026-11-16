#!/bin/bash
cd /home/claude/chb-pages
python3 gen/rw/timefix.py && python3 gen/rw/dashfix.py && python3 gen/merge_rw.py && python3 gen/polish.py && python3 gen/nosrc.py && python3 gen/fixes.py && python3 gen/interlink.py && python3 gen/measure.py | head -2 && python3 gen/finish.py 2>&1 | tail -1
git add -A; git commit -qm "$1

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XzVF5gGxAc3JvRFXnQXt9Y"; git -c push.negotiate=true push -q origin HEAD && echo pushed
