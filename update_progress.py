#!/usr/bin/env python3
"""
YoctoQuest Progress Auto-Updater
Automatically updates all stats in learning-journal.md based on checked items
"""

import re
from datetime import datetime
from pathlib import Path

# XP values for different activities
XP_VALUES = {
    'System Requirements': 30,
    'Tools Installation': 40,
    'What is Yocto?': 20,
    'Architecture Overview': 25,
    'Key Concepts (BitBake, Layers, Recipes)': 30,
    'Poky Setup': 40,
    'First Build (core-image-minimal)': 80,
    'Build Directory Structure': 30,
    'Recipe Syntax (.bb files)': 25,
    'Writing Your First Recipe': 50,
    'Recipe Variables & Functions': 30,
    'Understanding Layers': 25,
    'Creating Custom Layer': 60,
    'Layer Priority & Configuration': 30,
    'Image Types & Classes': 25,
    'Custom Image Creation': 70,
    'Package Groups': 30,
    '.bbappend Files': 40,
    'Package Management (rpm/deb/ipk)': 35,
    'Kernel Customization': 100,
    'Machine Configurations': 50,
    'BSP Layer Development': 80,
    'SDK Generation': 60,
    'Cross-compilation with SDK': 70,
    'Common Build Errors': 40,
    'BitBake Debugging Tools': 50,
    'Log Analysis': 45,
}

BADGE_XP = 100

MODULE_TASKS = {
    '00': 3, '01': 4, '02': 5, '03': 4, '04': 4, '05': 3,
    '06': 4, '07': 3, '08': 3, '09': 4, '10': 3
}


def create_progress_bar(percent, length=10):
    """Create a visual progress bar"""
    filled = int(percent / 100 * length)
    return f"[{'█' * filled}{'░' * (length - filled)}]"


def create_confidence_bar(level):
    """Create confidence bar based on completion"""
    # 0=not started, 1-2=beginner, 3=learning, 4=comfortable, 5=proficient/expert
    bars = ['░░░░░', '█░░░░', '██░░░', '███░░', '████░', '█████']
    return bars[min(level, 5)]


def parse_learning_tracker(content):
    """Parse learning progress tracker and calculate stats"""
    module_stats = {}
    total_xp = 0
    completed_tasks = 0
    total_tasks = 0
    
    # Find learning tracker section
    tracker_match = re.search(
        r'## 📚 LEARNING PROGRESS TRACKER.*?\n\| Module.*?\n\|:.*?\n((?:\|.*?\n)+)',
        content, re.DOTALL
    )
    
    if not tracker_match:
        return None, 0, 0, 0
    
    tracker_lines = tracker_match.group(1).strip().split('\n')
    
    for line in tracker_lines:
        if not line.strip() or not line.startswith('|'):
            continue
            
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) < 6:
            continue
            
        module = parts[0].replace('*', '')
        topic = parts[1]
        status = parts[2]
        xp_earned = parts[4]
        
        # Count completed tasks
        if '✅' in status or '⭐' in status:
            total_tasks += 1
            completed_tasks += 1
            
            # Add XP if not already counted
            if xp_earned == '0':
                xp = XP_VALUES.get(topic, 20)
                total_xp += xp
            else:
                try:
                    total_xp += int(xp_earned)
                except:
                    pass
                    
            # Track by module
            if module not in module_stats:
                module_stats[module] = {'completed': 0, 'total': MODULE_TASKS.get(module, 3), 'xp': 0}
            module_stats[module]['completed'] += 1
            module_stats[module]['xp'] += XP_VALUES.get(topic, 20)
        else:
            total_tasks += 1
            if module not in module_stats:
                module_stats[module] = {'completed': 0, 'total': MODULE_TASKS.get(module, 3), 'xp': 0}
    
    return module_stats, total_xp, completed_tasks, total_tasks


def parse_badges(content):
    """Count completed badges"""
    badge_section = re.search(
        r'## 🏆 ACHIEVEMENT BADGES.*?\n\| Badge.*?\n\|:.*?\n((?:\|.*?\n)+)',
        content, re.DOTALL
    )
    
    if not badge_section:
        return 0, 0
    
    badge_lines = badge_section.group(1).strip().split('\n')
    total_badges = len([l for l in badge_lines if l.strip() and l.startswith('|')])
    completed_badges = len([l for l in badge_lines if '✅' in l])
    
    return completed_badges, total_badges


def parse_quest_log_time(content):
    """Calculate total time spent today from Quest Log"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    quest_section = re.search(
        r'## 📝 QUEST LOG.*?\n\| Date.*?\n\|:.*?\n((?:\|.*?\n)+)',
        content, re.DOTALL
    )
    
    if not quest_section:
        return "0m"
    
    quest_lines = quest_section.group(1).strip().split('\n')
    total_minutes = 0
    
    for line in quest_lines:
        if today in line and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                time_str = parts[4]  # Time column (now 5th column without XP and Level)
                # Parse time formats: "2h", "1.5h", "30m", "2h 30m"
                hours = 0
                minutes = 0
                
                if 'h' in time_str:
                    if ' ' in time_str:
                        # Format: "2h 30m"
                        time_parts = time_str.split()
                        for part in time_parts:
                            if 'h' in part:
                                hours = float(part.replace('h', ''))
                            elif 'm' in part:
                                minutes = float(part.replace('m', ''))
                    else:
                        # Format: "2h" or "1.5h"
                        hours = float(time_str.replace('h', ''))
                elif 'm' in time_str:
                    # Format: "30m"
                    minutes = float(time_str.replace('m', ''))
                
                total_minutes += (hours * 60) + minutes
    
    # Convert back to hours and minutes
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    
    if hours > 0 and minutes > 0:
        return f"{hours}h {minutes}m"
    elif hours > 0:
        return f"{hours}h"
    elif minutes > 0:
        return f"{minutes}m"
    else:
        return "0m"


def check_badge_achievements(content, module_stats):
    """Automatically check and date badges based on completed tasks"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Define badge unlock conditions based on learning tracker
    badge_conditions = {
        '🚀': {
            'name': 'First Launch',
            'check': lambda: any('First Build (core-image-minimal)' in line and '✅' in line 
                              for line in content.split('\n'))
        },
        '📦': {
            'name': 'Recipe Master',
            'check': lambda: any('Writing Your First Recipe' in line and '✅' in line 
                              for line in content.split('\n'))
        },
        '🖼️': {
            'name': 'Image Architect',
            'check': lambda: any('Custom Image Creation' in line and '✅' in line 
                              for line in content.split('\n'))
        },
        '🛠️': {
            'name': 'SDK Wielder',
            'check': lambda: any('SDK Generation' in line and '✅' in line 
                              for line in content.split('\n'))
        },
        '🎨': {
            'name': 'Layer Craftsman',
            'check': lambda: any('Creating Custom Layer' in line and '✅' in line 
                              for line in content.split('\n'))
        },
        '🐛': {
            'name': 'Bug Slayer',
            'check': lambda: any('BitBake Debugging Tools' in line and '✅' in line 
                              for line in content.split('\n'))
        }
    }
    
    # Update badge statuses
    def replace_badge(match):
        parts = match.group(0).split('|')
        badge_emoji = parts[1].strip()
        title = parts[2].strip()
        desc = parts[3].strip()
        status = parts[4].strip()
        date_unlocked = parts[5].strip()
        
        # Check if this badge should be unlocked or locked
        if badge_emoji in badge_conditions:
            condition = badge_conditions[badge_emoji]
            if condition['check']():
                # Auto-unlock the badge
                if '☐' in status:
                    status = '✅'
                    date_unlocked = today
                elif '✅' in status and (not date_unlocked or date_unlocked == '-'):
                    date_unlocked = today
            else:
                # Task is not completed - uncheck badge
                if '✅' in status or '⭐' in status:
                    status = '☐'
                    date_unlocked = '-'
        
        return f"| {badge_emoji} | {title} | {desc} | {status} | {date_unlocked} |"
    
    # Update all badge rows
    pattern = r'\| [🚀📦🖼️🛠️🔥🐛🎨⚡] \| .+? \| .+? \| .+? \| .+? \|'
    content = re.sub(pattern, replace_badge, content)
    
    return content


def get_level_info(xp):
    """Determine current level based on XP"""
    if xp < 250:
        level = "🌱 **Apprentice**"
        stage = 1
        progress = int((xp / 250) * 100)
        next_level = 250 - xp
    elif xp < 600:
        level = "🔨 **Craftsman**"
        stage = 2
        progress = int(((xp - 250) / 350) * 100)
        next_level = 600 - xp
    elif xp < 1200:
        level = "⚔️ **Warrior**"
        stage = 3
        progress = int(((xp - 600) / 600) * 100)
        next_level = 1200 - xp
    else:
        level = "👑 **Yocto Master**"
        stage = 4
        progress = 100
        next_level = 0
    
    return level, stage, progress, next_level


def update_learning_tracker_xp(content):
    """Update XP values in learning tracker based on completed items"""
    def replace_line(match):
        parts = match.group(0).split('|')
        module = parts[1].strip()
        topic = parts[2].strip()
        status = parts[3].strip()
        confidence = parts[4].strip()
        xp_earned = parts[5].strip()
        notes = parts[6].strip()
        
        # If completed but XP is 0, update it
        if ('✅' in status or '⭐' in status):
            xp = XP_VALUES.get(topic, 20)
            # Estimate confidence based on completion
            if '⭐' in status:
                conf_bar = create_confidence_bar(5)
            elif '✅' in status:
                conf_bar = create_confidence_bar(3)
            else:
                conf_bar = confidence
            
            # Add date if missing
            if not notes or notes == '' or notes == '-':
                notes = datetime.now().strftime('%Y-%m-%d')
            
            return f"| {module} | {topic} | {status} | `{conf_bar}` | {xp} | {notes} |"
        
        # If NOT completed, reset XP and confidence
        elif '☐' in status or '⏳' in status:
            # Keep confidence if in progress, reset if not started
            if '☐' in status:
                conf_bar = create_confidence_bar(0)
                notes = ''
                xp = 0
            else:  # ⏳ in progress
                # Keep current confidence or set to beginner
                conf_bar = confidence if confidence != '`░░░░░`' else create_confidence_bar(1)
                xp = 0
            
            return f"| {module} | {topic} | {status} | `{conf_bar}` | {xp} | {notes} |"
        
        return match.group(0)
    
    # Update learning tracker rows - match with flexible spacing at end
    pattern = r'\| \*\*\d+\*\* \| .+? \| .+? \| `.+?` \| \d+ \| .*?\|'
    content = re.sub(pattern, replace_line, content)
    
    return content


def update_module_tracker(content, module_stats):
    """Update module completion tracker"""
    def replace_module(match):
        parts = match.group(0).split('|')
        module_num = parts[1].strip()
        name = parts[2].strip()
        
        if module_num in module_stats:
            stats = module_stats[module_num]
            completed = stats['completed']
            total = stats['total']
            xp = stats['xp']
            percent = int((completed / total) * 100) if total > 0 else 0
            progress_bar = create_progress_bar(percent)
            
            if completed == total:
                status = '✅'
            elif completed > 0:
                status = '⏳'
            else:
                status = '☐'
            
            return f"| {module_num} | {name} | `{progress_bar}` {percent}% | {completed}/{total} | {xp} | {status} |"
        
        return match.group(0)
    
    pattern = r'\| \d+ \| .+? \| `.+?` \d+% \| \d+/\d+ \| \d+ \| .+? \|'
    content = re.sub(pattern, replace_module, content)
    
    return content


def update_dashboard(content, total_xp, completed_badges, total_badges, completed_modules, session_time):
    """Update the player dashboard"""
    level, stage, level_progress, next_xp = get_level_info(total_xp)
    
    # Calculate overall XP progress (out of 1000 for visual bar)
    xp_percent = min(int((total_xp / 1000) * 10), 10)
    xp_bar = '█' * xp_percent + '░' * (10 - xp_percent)
    
    # Badge bar
    badge_percent = int((completed_badges / total_badges) * 5) if total_badges > 0 else 0
    badge_bar = '█' * badge_percent + '░' * (5 - badge_percent)
    
    # Module bar
    module_percent = int((completed_modules / 11) * 11)
    module_bar = '█' * module_percent + '░' * (11 - module_percent)
    
    # Get level emoji
    level_emoji = level.split()[0]
    level_name = ' '.join(level.split()[1:]).replace('*', '')
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Update dashboard
    # Match the table format dashboard
    dashboard_pattern = r'\| 🎯 \*\*CURRENT LEVEL\*\*.*?\n\|:.*?\n\| ⚡.*?\n\| 🏆.*?\n\| 📚.*?\n\| 🔥.*?\n\n\*\*Last Updated:\*\* `[\d-]+`'
    
    # Create a markdown-friendly dashboard without box drawing (better rendering)
    # Use a table format which renders consistently - centered alignment
    
    new_dashboard = f'''| 🎯 **CURRENT LEVEL** | **{level_name.replace("*", "")}** | Stage {stage}/4 |
|:--------------------:|:---------------------------------:|:---------------:|
| ⚡ **Total XP** | **{total_xp} / 1000** | `{create_progress_bar(min(int(total_xp/10), 10), 10)}` |
| 🏆 **Badges Earned** | **{completed_badges} / 8** | `{create_progress_bar(int(completed_badges/8*5), 5)}` |
| 📚 **Modules Complete** | **{completed_modules} / 11** | `{create_progress_bar(int(completed_modules/11*11), 11)}` |
| 🔥 **Current Streak** | **1 days** | Keep going! |

**Last Updated:** `{today}`'''
    
    content = re.sub(dashboard_pattern, new_dashboard, content, flags=re.DOTALL | re.MULTILINE)
    
    # Update last updated date
    content = re.sub(
        r'\*\*Last Updated:\*\* `[\d-]+`',
        f'**Last Updated:** `{today}`',
        content
    )
    
    # Update session time
    content = re.sub(
        r'\*\*Session Time Today:\*\* `.+?`',
        f'**Session Time Today:** `{session_time}`',
        content
    )
    
    # Update mastery progression
    level_pattern = r'\| \*\*1\*\* \| 🌱 \*\*Apprentice\*\* \| 0 - 250 \| `.+?` \d+% \| .+? \| .+? \|'
    new_level = f"| **1** | 🌱 **Apprentice** | 0 - 250 | `{create_progress_bar(level_progress)}` {level_progress}% | *Basics & Setup* | ✅ {'CURRENT' if stage == 1 else 'DONE'} |"
    content = re.sub(level_pattern, new_level, content)
    
    if stage >= 2:
        level2_pattern = r'\| \*\*2\*\* \| 🔨 \*\*Craftsman\*\* \| 250 - 600 \| `.+?` \d+% \| .+? \| .+? \|'
        prog2 = level_progress if stage == 2 else 100
        new_level2 = f"| **2** | 🔨 **Craftsman** | 250 - 600 | `{create_progress_bar(prog2)}` {prog2}% | *Building & Recipes* | ✅ {'CURRENT' if stage == 2 else 'DONE'} |"
        content = re.sub(level2_pattern, new_level2, content)
    
    if stage >= 3:
        level3_pattern = r'\| \*\*3\*\* \| ⚔️ \*\*Warrior\*\* \| 600 - 1200 \| `.+?` \d+% \| .+? \| .+? \|'
        prog3 = level_progress if stage == 3 else 100
        new_level3 = f"| **3** | ⚔️ **Warrior** | 600 - 1200 | `{create_progress_bar(prog3)}` {prog3}% | *Debugging & Layers* | ✅ {'CURRENT' if stage == 3 else 'DONE'} |"
        content = re.sub(level3_pattern, new_level3, content)
    
    if stage >= 4:
        level4_pattern = r'\| \*\*4\*\* \| 👑 \*\*Yocto Master\*\* \| 1200\+ \| `.+?` \d+% \| .+? \| .+? \|'
        new_level4 = f"| **4** | 👑 **Yocto Master** | 1200+ | `{create_progress_bar(level_progress)}` {level_progress}% | *Architecture & BSP* | ✅ CURRENT |"
        content = re.sub(level4_pattern, new_level4, content)
    
    return content


def main():
    journal_path = Path(__file__).parent / 'README.md'
    
    if not journal_path.exists():
        print(f"❌ Error: {journal_path} not found!")
        return
    
    print("🎮 YoctoQuest Progress Updater")
    print("=" * 50)
    
    # Read the journal
    content = journal_path.read_text(encoding='utf-8')
    
    # Parse current state
    module_stats, total_xp, completed_tasks, total_tasks = parse_learning_tracker(content)
    completed_badges, total_badges = parse_badges(content)
    completed_modules = len([m for m, s in module_stats.items() if s['completed'] == s['total']])
    
    # Add badge XP
    total_xp += completed_badges * BADGE_XP
    
    print(f"📊 Current Stats:")
    print(f"   ⚡ Total XP: {total_xp}")
    print(f"   ✅ Tasks Completed: {completed_tasks}/{total_tasks}")
    print(f"   🏆 Badges Earned: {completed_badges}/{total_badges}")
    print(f"   📚 Modules Complete: {completed_modules}/11")
    
    level, stage, progress, next_xp = get_level_info(total_xp)
    print(f"   🎯 Current Level: {level} (Stage {stage}/4)")
    if next_xp > 0:
        print(f"   📈 Next Level: {next_xp} XP away")
    
    # Update content
    print("\n🔄 Updating progress...")
    content = update_learning_tracker_xp(content)
    content = check_badge_achievements(content, module_stats)  # Auto-check badges
    
    # Re-parse badges after auto-checking
    completed_badges, total_badges = parse_badges(content)
    total_xp = 0
    for m, s in module_stats.items():
        total_xp += s['xp']
    total_xp += completed_badges * BADGE_XP
    
    # Parse session time from quest log
    session_time = parse_quest_log_time(content)
    
    content = update_module_tracker(content, module_stats)
    content = update_dashboard(content, total_xp, completed_badges, total_badges, completed_modules, session_time)
    
    # Write back
    journal_path.write_text(content, encoding='utf-8')
    
    print("✅ Progress updated successfully!")
    print(f"\n💡 Tip: Just check ✅ items in the tracker, then run this script!")

if __name__ == '__main__':
    main()
