# Telegram Currency Bot with Selenium Parser

A Telegram bot written in Python that automatically retrieves and displays current exchange rates for **USD**, **EUR**, and **RUB** using **Selenium Web Scraping**.

## Features

- Telegram Bot integration
- Selenium-based web scraping
- Retrieves live exchange rates
- Supports:
  - USD (US Dollar)
  - EUR (Euro)
  - RUB (Russian Ruble)
- Simple and lightweight architecture
- Easy deployment on Linux servers, Docker, or AWS EC2

## Technologies Used

- Python 3.x
- Selenium
- TeleBot (pyTelegramBotAPI)
- ChromeDriver
- Requests
- BeautifulSoup (optional)

## Project Structure

```text
project/
│
├── main.py
├── parser.py
├── config.py
├── requirements.txt
├── telebot.png
└── README.md
````

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/telegram-currency-bot.git
cd telegram-currency-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Requirements

Example `requirements.txt`:

```text
pyTelegramBotAPI
selenium
webdriver-manager
requests
```

## Configuration

Create a bot using **@BotFather** on Telegram and obtain your bot token.

Update your token in the project:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

## Running the Bot

```bash
python main.py
```

## Bot Commands

| Command | Description                    |
| ------- | ------------------------------ |
| /start  | Start the bot                  |
| USD     | Show current USD exchange rate |
| EUR     | Show current EUR exchange rate |
| RUB     | Show current RUB exchange rate |

## Selenium Parser

The parser uses Selenium to:

1. Open the target currency exchange website.
2. Extract exchange rate data.
3. Return parsed values to the Telegram bot.
4. Display the latest rates to users.

## Example Output

```text
💵 USD: 387.50 AMD
💶 EUR: 421.80 AMD
₽ RUB: 4.85 AMD
```

## Deployment

### Docker

```bash
docker build -t telegram-currency-bot .
docker run -d telegram-currency-bot
```

### AWS EC2

```bash
sudo apt update
sudo apt install python3 python3-pip -y

git clone <repository-url>
cd telegram-currency-bot

pip install -r requirements.txt
python main.py
```

## Future Improvements

* Support additional currencies
* Historical exchange rates
* Exchange rate charts
* Database storage
* Admin panel
* Scheduled notifications

## Author

Albert Zaqaryan

GitHub: [https://github.com/AlbertZaqaryan](https://github.com/AlbertZaqaryan)

## License

This project is licensed under the MIT License.

```
```
