# 🎮 Guess Game - Web Interface

A modern, interactive web version of the classic Guess Game with both word and number guessing modes.

## 🚀 Features

- **Two Game Modes**: Word guessing and number guessing
- **Modern UI**: Beautiful, responsive design with animations
- **Real-time Feedback**: Instant hints and progress tracking
- **Game History**: Track all your guesses and results
- **Keyboard Support**: Use Enter to submit, Escape to go back
- **Mobile Friendly**: Responsive design for all devices

## 🎯 Game Modes

### 🔤 Word Guessing
- Guess from 8 programming-related words
- 5 attempts to find the secret word
- Hint revealed after 2 failed attempts
- Words: python, computer, programming, gemini, miniproject, development, challenge, algorithm

### 🔢 Number Guessing
- Guess a number between 1 and 100
- 5 attempts to find the secret number
- Hints after each guess (higher/lower)
- Smart feedback system

## 🛠️ How to Run

### Option 1: Direct Browser
1. Navigate to the `Game` folder
2. Double-click `game_web.html`
3. The game will open in your default browser

### Option 2: Local Server (Recommended)
1. Open terminal/command prompt
2. Navigate to the `Game` folder
3. Start a simple HTTP server:

**Python 3:**
```bash
python -m http.server 8000
```

**Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

4. Open browser and go to `http://localhost:8000/game_web.html`

## 🎮 How to Play

1. **Choose Your Game**: Click on either Word Guessing or Number Guessing
2. **Make Your Guess**: Type your guess and press Enter or click Submit
3. **Get Feedback**: See hints and track your progress
4. **Win or Try Again**: Keep guessing until you win or run out of attempts
5. **Play Again**: Start a new game with different secret values

## ⌨️ Keyboard Shortcuts

- **Enter**: Submit your guess
- **Escape**: Go back to game selection
- **Tab**: Navigate between input fields

## 🎨 Features

- **Smooth Animations**: Fade-in effects and hover animations
- **Color-coded Feedback**: Green for correct, red for incorrect, yellow for hints
- **Progress Tracking**: Visual attempt counter and game history
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Accessibility**: Clear visual feedback and intuitive navigation

## 🔧 Technical Details

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **No Dependencies**: Pure vanilla JavaScript - no frameworks required
- **Cross-browser**: Compatible with all modern browsers
- **Offline Ready**: Works without internet connection

## 🎯 Game Logic

The web version replicates the exact functionality of your Python `Guess_Game.py`:
- Same word list and number range
- Same attempt limit (5)
- Same hint system
- Same win/lose conditions

## 🚀 Future Enhancements

- Sound effects and music
- High score tracking
- Multiple difficulty levels
- Custom word lists
- Multiplayer support
- Dark/light theme toggle

## 📱 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🎉 Enjoy Playing!

The Guess Game web interface provides the same fun gameplay as your Python version, but with a beautiful, modern interface that's easy to use on any device!
