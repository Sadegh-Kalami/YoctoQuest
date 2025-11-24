# YoctoQuest 🎮

I love games and I'm in love with embedded Linux. So let's have a Yocto Quest!

## What This Is

A gamified learning path to master the Yocto Project. 27 topics, 11 modules, 8 badges to unlock. Track what you learn, level up from Apprentice to Yocto Master, and build real embedded Linux skills along the way.

## How It Works

1. **Learn** - Study a topic, build something, read docs
2. **Check off** - Mark it complete in `notes/learning-journal.md`
3. **Track** - Run `python3 update_progress.py` to update stats automatically

Build files stay outside this repo (e.g., `~/yocto-build`). This repo is just notes, configs, and learning progress.

## Learning Path

**27 topics across 11 modules:**
Prerequisites → Fundamentals → Build System → Recipes → Layers → Images → Advanced Topics → BSP → SDK → Debugging → Projects

Check `notes/learning-journal.md` for the full breakdown and current progress.

## Quick Start

```bash
# 1. Open the learning journal
code notes/learning-journal.md

# 2. Learn something and check it off (✅)

# 3. Update your stats
python3 update_progress.py
```

## Rules

- Build outputs live in `~/yocto-build/` (not in this repo)
- Only commit notes, configs, and scripts
- Check off topics honestly - this is for your learning, not show
- Use the Quest Log to remember what worked and what didn't
