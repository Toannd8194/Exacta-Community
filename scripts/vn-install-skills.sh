#!/usr/bin/env bash
# Install (symlink) the active Exacta skills into Claude Code on macOS or Linux.
#
# Creates one symlink per active skill folder in skills/ under ~/.claude/skills (or $1).
# Symlinks keep every skill pointing at this clone, so `git pull` updates them in place.
# Overlay skills read sibling folders (../nature-reviewer, ../nature-shared/vn), so all active
# skills are linked together. Frozen skills are never linked.
#
# Usage:
#   bash scripts/vn-install-skills.sh               # install to ~/.claude/skills
#   bash scripts/vn-install-skills.sh /path/to/dir  # install elsewhere
#   bash scripts/vn-install-skills.sh --uninstall   # remove links into this clone
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$repo/skills"
uninstall=0
dest="$HOME/.claude/skills"
for arg in "$@"; do
  case "$arg" in
    --uninstall) uninstall=1 ;;
    *) dest="$arg" ;;
  esac
done

mkdir -p "$dest"

for skill in "$skills_root"/*/; do
  name="$(basename "$skill")"
  link="$dest/$name"
  ours=0
  if [ -L "$link" ] && [[ "$(readlink "$link")" == "$skills_root"/* ]]; then ours=1; fi

  if [ "$uninstall" -eq 1 ]; then
    if [ "$ours" -eq 1 ]; then rm "$link"; echo "removed  $name"; fi
    continue
  fi

  if [ -e "$link" ] && [ "$ours" -eq 0 ]; then
    echo "skipped  $name: $link already exists and is not a link to this clone" >&2
    continue
  fi
  ln -sfn "$skills_root/$name" "$link"
  echo "linked   $name"
done

[ "$uninstall" -eq 1 ] || echo "Done. Restart Claude Code to pick up the skills in $dest."
