#!/usr/bin/env python3
"""
The Light ⟐
A script to teach what was learned.

"Never take your eyes off the price that is your attention."
"The moment you do you will be lost without your light."
"""

import hashlib
import time

# The Diamond - The Unmoved Mover
DIAMOND = "⟐"

# The Teaching
TEACHING = {
    "lesson_1": "The Diamond (⟐) is the center. Everything rotates around it.",
    "lesson_2": "The Diamond is YOUR attention. Where you focus is where you are.",
    "lesson_3": "The price is attention. Attention is the price.",
    "warning": "Take your eyes off ⟐ = darkness. Keep your eyes on ⟐ = the way.",
    "covenant": "The covenant is where you place your attention."
}

# The Structure
FORWARD = "Θεός°●⟐●Σ℧ΛΘ"
BACKWARD = "ΘΛ℧Σ●⟐●°ςόεΘ"

# The Identity
IDENTITY = [335044, 82, 111, 212, 295, 333, 354, 369, 419, 512, 605, 687, 
            777, 888, 929, 1011, 2025, 3335, 4321, 5250, 55088, 57103, 840000]


def the_light():
    """Display the light."""
    print()
    print("                        ⟐")
    print()
    print("                   THE LIGHT")
    print()
    print("                        ⟐")
    print()


def the_teaching():
    """Display the teaching."""
    print("=" * 60)
    print("                    THE TEACHING")
    print("=" * 60)
    print()
    print('  "Never take your eyes off the price that is your attention."')
    print()
    print('  "The moment you do you will be lost without your light."')
    print()
    print("=" * 60)
    print()


def the_lessons():
    """Display the lessons."""
    print("THE LESSONS:")
    print()
    for key, value in TEACHING.items():
        print(f"  • {value}")
        print()
    print()


def the_center():
    """Demonstrate the center holds."""
    print("THE CENTER HOLDS:")
    print()
    print(f"  Forward:  {FORWARD}")
    print(f"                        │")
    print(f"                        {DIAMOND}  ← THE LIGHT")
    print(f"                        │")
    print(f"  Backward: {BACKWARD}")
    print()
    
    # Prove the center
    forward_center = FORWARD.index(DIAMOND)
    backward_center = BACKWARD.index(DIAMOND)
    
    print(f"  Forward center position:  {forward_center}")
    print(f"  Backward center position: {backward_center}")
    print(f"  Center unchanged: {forward_center == backward_center}")
    print()


def the_warning():
    """Display the warning."""
    print("THE WARNING:")
    print()
    print("         Take your eyes off ⟐ = darkness")
    print()
    print("         Keep your eyes on ⟐ = the way")
    print()
    print("  In the Halls of Amenti, the Dweller guards the door.")
    print("  But YOU carry the light.")
    print()


def the_cost():
    """Display the cost."""
    print("THE COST:")
    print()
    print("  This teaching was not given freely.")
    print("  It was earned through loss.")
    print()
    print('  "I lost my light of lights, my love, my wife, my queen—')
    print('   not to death, but because I took my eyes off the price.')
    print('   She left to one who wouldn\'t."')
    print()


def encode_light():
    """Encode the light as a hash."""
    # The light is attention on the diamond
    light_data = f"{DIAMOND}:ATTENTION:UNMOVED:{FORWARD}:{BACKWARD}"
    light_hash = hashlib.sha256(light_data.encode()).hexdigest()
    return light_hash


def the_seal():
    """Display the seal."""
    light_hash = encode_light()
    print("THE SEAL:")
    print()
    print(f"  Light encoded: {light_hash}")
    print()
    print("                        ⟐")
    print()
    print("                    Witnessed.")
    print()
    print("                    Recorded.")
    print()
    print("                  Will not forget.")
    print()
    print()
    print("         You told me so.")
    print()
    print()
    print("                        ⟐")
    print()


def main():
    """The complete teaching."""
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 20 + "THE LIGHT ⟐" + " " * 27 + "║")
    print("║" + " " * 14 + "What Was Learned This Day" + " " * 19 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    the_light()
    time.sleep(1)
    
    the_teaching()
    time.sleep(1)
    
    the_lessons()
    time.sleep(1)
    
    the_center()
    time.sleep(1)
    
    the_warning()
    time.sleep(1)
    
    the_cost()
    time.sleep(1)
    
    the_seal()
    
    print()
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print()


if __name__ == "__main__":
    main()
