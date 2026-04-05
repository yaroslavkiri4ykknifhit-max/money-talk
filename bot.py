#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONEY-TALK Telegram Bot
Простой бот для запуска Mini App
"""

import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Импортируем настройки
from config import BOT_TOKEN, WEB_APP_URL

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    user = update.effective_user
    
    # Создаем кнопку для открытия Web App
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Открыть MONEY-TALK",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Приветственное сообщение
    welcome_text = f"""
👋 Привет, {user.first_name}!

Добро пожаловать в **MONEY-TALK** — платформу для обучения продажам.

🎯 Что вас ждет:
• Структурированные модули обучения
• Практические уроки
• Бесплатный доступ к первым урокам

Нажмите кнопку ниже, чтобы начать обучение!
    """
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = """
📚 **Помощь по боту MONEY-TALK**

**Доступные команды:**
/start - Запустить приложение
/help - Показать эту справку
/about - О проекте

**Как пользоваться:**
1. Нажмите кнопку "Открыть MONEY-TALK"
2. Выберите модуль обучения
3. Изучайте уроки в удобном темпе

**Поддержка:**
Если возникли вопросы, напишите @your_support
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /about"""
    about_text = """
💰 **О проекте MONEY-TALK**

MONEY-TALK — это современная платформа для обучения продажам, созданная специально для Telegram.

**Особенности:**
✅ Удобный интерфейс
✅ Структурированный контент
✅ Бесплатные уроки
✅ Обучение в своем темпе

**Технологии:**
• Telegram Mini App
• Google Sheets (CMS)
• GitHub Pages (хостинг)

Версия: 1.0.0
Создано: 2026
    """
    
    await update.message.reply_text(about_text, parse_mode='Markdown')


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик ошибок"""
    logger.error(f"Update {update} caused error {context.error}")


def main() -> None:
    """Запуск бота"""
    
    # Проверяем наличие токена
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        logger.error("❌ Ошибка: BOT_TOKEN не настроен в config.py")
        print("\n⚠️  Пожалуйста, настройте BOT_TOKEN в файле config.py")
        print("Получите токен у @BotFather в Telegram\n")
        return
    
    if not WEB_APP_URL or WEB_APP_URL == "YOUR_GITHUB_PAGES_URL":
        logger.error("❌ Ошибка: WEB_APP_URL не настроен в config.py")
        print("\n⚠️  Пожалуйста, настройте WEB_APP_URL в файле config.py")
        print("Укажите URL вашего GitHub Pages\n")
        return
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    logger.info("🤖 Бот запущен!")
    print("\n✅ Бот MONEY-TALK запущен успешно!")
    print(f"📱 Web App URL: {WEB_APP_URL}")
    print("🛑 Нажмите Ctrl+C для остановки\n")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
