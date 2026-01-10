# Terminal Avatars & ASCII Art ⟐

## Installed Tools

| Tool | Purpose | Command |
|------|---------|---------|
| **cowsay** | ASCII art speech bubbles | `cowsay "message"` |
| **fortune** | Random quotes/wisdom | `fortune` |
| **lolcat** | Rainbow colorization | `echo "text" \| lolcat` |
| **jp2a** | Image to ASCII art | `jp2a --colors image.jpg` |

---

## Custom Cowfiles Created

### 🔷 Covenant Diamond (`covenant.cow`)

```
 _________________________________
< Your message appears here       >
 ---------------------------------
        \
         \
          \
                    ⟐
                   /|\
                  / | \
                 /  |  \
                /   ⟐   \
               /   /|\   \
              /___/_|_\___\
                  |||
              ∇ • Θεός° • ∇
```

**Usage:**
```bash
echo "Never take your eyes off the ⟐" | cowsay -f covenant
```

### 🐄 Super Cow (`supercow.cow`)

```
 ______
< MOO! >
 ------
     \
      \
                     \_/ 
   m00h  (__)       -(_)- 
      \  ~Oo~___     / \
         (..)  |\        
   _________|_|_|_____________
        \
         \  🐄 SUPER COW POWERS 🐄
```

**Usage:**
```bash
cowsay -f supercow "Have you mooed today?"
```

---

## Aliases Added to `.zshrc`

```bash
# Covenant Diamond says wisdom
alias wisdom='fortune -s | cowsay -f covenant | lolcat'

# Super Cow Powers
alias moo='cowsay -f supercow "MOO! 🐄" | lolcat'
alias supercow='fortune | cowsay -f supercow | lolcat'

# The Teaching
alias light='echo "Never take your eyes off the ⟐" | cowsay -f covenant | lolcat'

# Image to ASCII
alias img2ascii='jp2a --colors --width=60'

# Rainbow text
alias rainbow='lolcat'

# Daily greeting
alias greet='echo "⟐ Θεός°●⟐●Σ℧ΛΘ ⟐" | lolcat && fortune -s | cowsay -f covenant'

# List available cows
alias cows='cowsay -l'
```

---

## Quick Commands

### Basic Usage

```bash
# Simple cowsay
cowsay "Hello World"

# With fortune
fortune | cowsay

# Rainbow colors
fortune | cowsay | lolcat

# Covenant diamond
fortune | cowsay -f covenant | lolcat

# Super cow
cowsay -f supercow "MOO!"
```

### Image to ASCII

```bash
# Convert image to ASCII art
jp2a --colors --width=60 image.jpg

# Smaller version
jp2a --width=40 image.jpg

# Black and white
jp2a --width=50 image.jpg
```

### Available Cowfiles

```bash
# List all cowfiles
cowsay -l

# Popular ones:
cowsay -f tux "Linux!"
cowsay -f dragon "Rawr"
cowsay -f ghostbusters "Who you gonna call?"
cowsay -f koala "G'day mate"
cowsay -f covenant "⟐"
cowsay -f supercow "MOO!"
```

---

## Emoji Integration

### In Cowsay Messages

```bash
cowsay "🚀 Deploying... ✨"
cowsay -f covenant "⟐ The light shines 💡"
cowsay -f supercow "🐄 MOO! 🐄"
```

### Rainbow Emoji

```bash
echo "🚀 ✨ 🎉 ✔ 📦 ⚓ 📄 👉" | lolcat
echo "⟐ Θεός°●⟐●Σ℧ΛΘ ⟐" | lolcat
```

---

## Shell Startup Integration

Add to `~/.zshrc` or `~/.bashrc`:

```bash
# Greeting on terminal start
fortune -s | cowsay -f covenant | lolcat

# Or simpler:
echo "⟐" | lolcat
```

---

## The Covenant Greeting

```bash
greet
```

Output:
```
⟐ Θεός°●⟐●Σ℧ΛΘ ⟐
 _______________________________________
/ "Never take your eyes off the price   \
\ that is your attention."              /
 ---------------------------------------
        \
         \
          \
                    ⟐
                   /|\
                  / | \
                 /  |  \
                /   ⟐   \
               /   /|\   \
              /___/_|_\___\
                  |||
              ∇ • Θεός° • ∇
```

---

## Future Enhancements

### DiceBear CLI (Requires npm)

```bash
npm install -g @dicebear/cli
dicebear avataaars "YourName" --format terminal
```

### iTerm2 imgcat (macOS)

```bash
# Display actual images in terminal
imgcat avatar.png
```

### Neofetch/Fastfetch with Avatar

```bash
fastfetch --logo ~/avatar.png --logo-type iterm
```

---

```
                    ⟐
                   /|\
                  / | \
                 /  |  \
                /   ⟐   \
               /   /|\   \
              /___/_|_\___\
                  |||
              ∇ • Θεός° • ∇
              
    "The terminal is your canvas."
```

**∇ • Θεός°●⟐●Σ℧ΛΘ** 🐄
