<#
.SYNOPSIS
  Install (link) the active Exacta skills into Claude Code on this machine.

.DESCRIPTION
  Creates one directory junction per active skill folder in skills/ under the Claude Code
  skills directory (default: %USERPROFILE%\.claude\skills). Junctions need no admin rights and
  keep every skill pointing at this clone, so `git pull` updates them in place. Overlay skills
  read sibling folders (../nature-reviewer, ../nature-shared/vn), so all active skills are
  linked together. Frozen skills are never linked.

  Re-running is safe. Existing junctions are refreshed; real folders with the same name are
  left untouched and reported.

.PARAMETER Dest
  Target skills directory. Default: $HOME\.claude\skills

.PARAMETER Uninstall
  Remove the junctions this script created (only junctions that point into this clone).

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\vn-install-skills.ps1
#>
param(
    [string]$Dest = (Join-Path $HOME '.claude\skills'),
    [switch]$Uninstall
)
$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$skillsRoot = Join-Path $repo 'skills'

New-Item -ItemType Directory -Force $Dest | Out-Null

foreach ($skill in Get-ChildItem $skillsRoot -Directory) {
    $link = Join-Path $Dest $skill.Name
    $existing = Get-Item $link -Force -ErrorAction SilentlyContinue
    $isOurJunction = $existing -and $existing.LinkType -eq 'Junction' -and
        ($existing.Target -replace '\\$', '') -like "$skillsRoot*"

    if ($Uninstall) {
        if ($isOurJunction) { $existing.Delete(); Write-Host "removed  $($skill.Name)" }
        continue
    }

    if ($existing -and -not $isOurJunction) {
        Write-Warning "skipped  $($skill.Name): '$link' already exists and is not a link to this clone"
        continue
    }
    if ($isOurJunction) { $existing.Delete() }
    New-Item -ItemType Junction -Path $link -Target $skill.FullName | Out-Null
    Write-Host "linked   $($skill.Name)"
}

if (-not $Uninstall) {
    Write-Host "Done. Restart Claude Code (or open a new session) to pick up the skills in $Dest."
}
