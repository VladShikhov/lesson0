from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0,adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User('', '', 0)
        self.user_in_system = False
        
    def log_in(self, nickname, password):
        for i in range(self.users):
            if nickname == self.users[i].nickname and self.users[i].password == hash(password):
                self.current_user = self.users[i]
                self.user_in_system = True

    def register(self, nickname, password, age):
        self.user_ = User(nickname, password, age)
        if self.user_.nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(self.user_.nickname)
            self.current_user = self.user_.nickname
            self.user_in_system = True

    def log_out(self):
        self.current_user = None
        self.user_in_system = False

    def add(self, *other):
        print(len(other))
        for i in range(len(other)):          
            if other[i] in self.videos:
                continue
            else:
                self.videos.append(other[i].title)
                self.cens = other[i].adult_mode
                self.dur = other[i].duration
                self.time = other[i].time_now
        
    def get_videos(self, search):
        search_out = []
        search = search.lower()
        for i in range(len(self.videos)):            
            if search in self.videos[i].lower():
                search_out.append(self.videos[i])
        return search_out
    
    def watch_video(self, title_):
        if self.user_in_system == True:
            if self.user_.age < 18 and self.cens == True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:            
                for i in range(len(self.videos)):                    
                    if title_ == self.videos[i]:
                        for j in range(self.dur):                            
                            self.time += 1
                            print(self.time, end=' ')
                            sleep(0.1)
                        self.time = 0
                        print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
                   
                


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
