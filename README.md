# Netflix_Top_Genres(Python)
Данный репозиторий содержит исходные и итоговые файлы после проведения анализа данных по фильмам Netflix
Используемые библиотеки:
- Pandas
- Matplotlib
- Seaborn

Файлы содержат:

1. Исходный .csv файл, скачанный с ресурса https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download

   В нем находится таблица данных по фильмам и сериалам Netflix за последние 100 лет, а так же ряды дополнительной информации (рейтинг, описание и др.)

3. Файл .py , содержащий код на Python. В нём проводится следующие операции:
   - фильтрация данных, выведение только фильмов, выпущенных не ранее 2000 года;
   - группировка данных по году и жанру, подсчёт кол-ва фильмов в каждой группе;
   - ограчение ТОП 5 жанров по каждому году, а затем ТОП 1;
   - построение линейного графика на основе полученных данных о ТОП 5 жанров по каждому году, а затем построение столбчатой диаграммы по ТОП 1 жанру.
  
4. Файлы .png, на которых изображены графики из 2 пункта

5. .csv файлы, полученные путем выгрузки датафреймов, в которых содержатся итоговые таблицы из трех столбцов (Год, жанр, количество)
