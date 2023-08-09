Task 1
Открой файл distances.ipynb.

Объедини общие данные о фильмах tmdb_5000_movies и каст фильмов tmdb_5000_credits.
Оставь в датасете только фильмы, которые вышли в "релиз".
Убери фильмы с пропусками в колонках ['overview', 'genres', 'keywords'].
Выведи количество фильмов, оставшихся в выборке.
Task 2
Реализуем алгоритм рекомендации на основе описания фильма (overview) и ключевых слов к фильму (keywords). Объедини тексты этих колонок и проведи предобработку:

Замени NaN в описании фильма на пустой символ ''.
Удали все английские стоп-слова (используй параметр stop_words в TfidfVectorizer).
Рассчитай матрицу Tf-Idf для описания фильмов.
Выведи размер получившейся матрицы.

Параметр max_features в TfidfVectorizer должен быть равен 10000.

Task 3
Рассчитай cosine similarity между фильмами. Составь из этой матрицы pd.DataFrame. Для дальнейшего удобства, колонки и индексы таблицы назови согласноid фильма.
Сохрани получившийся DataFrame c расстояниями в папку assets с названием distance.csv. А сам объединенный датасет с фильмами сохрани в папку assets с названием movies.csv.

Получившиеся файлы distance.csv и movies.csv пушить в GitLab не нужно!

Task 4
Мы подготовили расстояния и данные о фильмах, теперь перейдем к реализации самого сервиса. Его основа находится в папке src. Для начала потребуется настроить переменные окружения для проекта. В файле .env укажи путь к файлам distance.csv и movies.csv.

Файл .env пушить в GitLab нельзя!!!

Task 5
Перейдем к самой реализации рекомендаций. Допиши метод recommendation, чтобы он возвращал top-k самых близких фильмов. Попробуй протестировать работу рекомендаций на серии фильмов ( например, "The Dark Knight" или "Pirates of the Caribbean").

Task 6
Хотелось бы, чтобы кроме названия фильма выводился бы и постер. В этом нам поможет OMDb API. Зарегистрируйся и получи api-key. Добавь его в файл .env. Допиши функцию _images_path, чтобы она отправляла запрос к OMDb-API и возвращала ссылку на постер фильма. Протестируй вывод постеров.

У бесплатного ключа лимит 1000 запросов в день.

Task 7
Чтобы улучшить рекомендации хотелось бы реализовать механизм фильтрации фильмов. Перед тем, как найти самые похожие фильмы по описанию, фильмы должны проходить фильтрацию по пользовательским параметрам. Реализуй фильтрацию фильмов по жанрам (genres) и по ещё одному параметру на твое усмотрение (это может быть год производства, режиссер, рейтинг фильма и т.п).

Для того, чтобы была возможность оставлять фильтр пустым, можно воспользоваться этим.

Основной функционал готов, теперь можно подумать и о дизайне. Поизучай галерею streamlit. Возможно ты найдешь там вдохновение, что бы ты хотел добавить к себе в сервис.