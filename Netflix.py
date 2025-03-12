import pandas as pd

file_path = r"C:\Users\USER\Desktop\py_proj\netflix_titles.csv"  # указываем путь
df = pd.read_csv(file_path)

# Разделяем жанры и создаем отдельные строки для каждого жанра
df_exploded = df.assign(listed_in=df["listed_in"].str.split(", ")).explode("listed_in")

# фильтруем только фильмы, вышедшие не ранее 2000-го года
movies_df = df_exploded[
    (df_exploded["type"] == "Movie") & (df_exploded["release_year"] >= 2000)
]

# группировка по году и жанру
top_genres_by_year = (
    movies_df.groupby(["release_year", "listed_in"])
    .size()
    .reset_index(name="count")
    .sort_values(["release_year", "count"], ascending=[True, False])
)

top_5_genres = top_genres_by_year.groupby("release_year").head(5)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 8))
sns.lineplot(
    data=top_5_genres, x="release_year", y="count", hue="listed_in", marker="o"
)

all_years = top_5_genres["release_year"].unique()  # Получаем все уникальные года
plt.xticks(all_years, rotation=45)  # Указываем все года и поворачиваем подписи

plt.title("ТОП 5 жанров фильмов Netflix по годам", fontsize=16)
plt.xlabel("Год выпуска", fontsize=12)
plt.ylabel("Количество фильмов", fontsize=12)


plt.legend(title="Жанр", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

plt.tight_layout()

plt.show()


# теперь выясним ТОП 1 жанр по кол-ву фильмов в каждом году

top_1_genre = top_5_genres.groupby("release_year").head(1)


sns.set_theme(style="whitegrid")  # Включаем сетку

plt.figure(figsize=(12, 6))
bar_plot = sns.barplot(
    data=top_1_genre, x="release_year", y="count", hue="listed_in", palette="viridis"
)
plt.title("ТОП-1 жанры Netflix по годам", fontsize=16)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Количество фильмов/сериалов", fontsize=12)
plt.xticks(rotation=45)  # Поворачиваем подписи по оси X для удобства

plt.legend(title="Жанр", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()  # Убираем наложение элементов
plt.show()

df = pd.DataFrame(top_5_genres)
df.to_excel("TOP_5_genres.xlsx", index=False)

df = pd.DataFrame(top_1_genre)
df.to_excel("TOP_1_genre.xlsx", index=False)
