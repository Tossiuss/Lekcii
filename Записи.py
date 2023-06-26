# isinstance(i, int)


# cd #папка с лекциями
# ls
# git init
# git add .
# git commit -m "ttt"
# git remote add origin #ссылка на репозиторий
# git push origin master



# при первой отправки версии кода
# git init -> инициализирует git репозиторий, создает директорию .git  
# (превращает текущую директорию в git репозиторий)
# git add . -> (отслеживание всех файлов) добавляет версии файла (снимки) в промежуточное пространство "индекс"
# git add <file_name> -> отслеживание конкретного файла
# git commit -m "massage" -> создание коммита (версии/слепка кода) с комментарием (сохранение версии кода  локальном git репозитории)
# git remote add origin <ssh/https> -> создание связи с удаленным репозитории на github
# git push origin <название ветки> (по умолчанию master, для mac main) -> отправка версии кода на удаленный репозиторий (git push origin master -> на ветку мастер)

# при повторной отправки  
# git add . 
# git commit -m "massage"
# git push origin master



# git status -> показывает статус или состояние файлов  
# git diff -> просмотр внесенных изменений 

# git checkout hash_commit -> переход к указанному коммиту 
# git log -> просмотр версии кода или коммиты 

# git branch <название ветки> -> создание указанной  ветки 
# git branch -> просмотр существующих веток 
# git checkout <название ветки> 
#                                  -> подключение или переход на указанную ветку
# git switch <название ветки>

# git pull origin master -> стягивание изменений с удаленного репозитория с указанной ветки (с github)

# git clone <url> -> склонировать или скачать удаленный репозиторий