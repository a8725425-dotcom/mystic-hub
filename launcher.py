import os
import json
import webbrowser

class MysticLauncher:
    def __init__(self):
        self.games = self.load_games()
    
    def load_games(self):
        # Загружаем список игр из файла
        if os.path.exists('games/games.json'):
            with open('games/games.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def show_games(self):
        print("🎮 MYSTIC PLATFORM - ДОСТУПНЫЕ ИГРЫ:")
        for i, game in enumerate(self.games, 1):
            print(f"{i}. {game['name']} - {game['author']}")
    
    def download_game(self, game_index):
        # Скачивание игры (пока просто копируем из папки)
        game = self.games[game_index]
        print(f"📥 Загружаем {game['name']}...")
        # Здесь будет логика загрузки
        print("✅ Игра загружена!")
    
    def run(self):
        while True:
            self.show_games()
            choice = input("\nВыбери игру (или 'q' для выхода): ")
            if choice == 'q':
                break
            try:
                self.download_game(int(choice) - 1)
            except:
                print("❌ Ошибка!")

# Запуск лаунчера
if __name__ == "__main__":
    launcher = MysticLauncher()
    launcher.run()