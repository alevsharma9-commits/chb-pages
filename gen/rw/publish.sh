#!/bin/bash
# Rebuild every page from the applied polished drafts, check, commit and push to main so the updater republishes.
cd /home/user/chb-pages || exit 1
for s in gen/rw/timefix.py gen/rw/dashfix.py gen/merge_rw.py gen/cleanbase.py gen/metaclean.py gen/humanfix.py gen/polish.py gen/nosrc.py gen/fixes.py gen/interlink.py gen/ctas.py; do python3 $s >/dev/null 2>&1 || { echo "FAILED $s"; exit 1; }; done
python3 gen/measure.py | head -2; python3 gen/finish.py 2>&1 | tail -1
git add -A; git commit -qm "${1:-Rebuild pages with polished drafts}" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01LqQvY38Vq37HVKLLtTrTgg"
git push -q origin HEAD && git push -q origin HEAD:main && echo pushed
