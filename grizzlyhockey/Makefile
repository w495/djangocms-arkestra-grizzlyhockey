PROJNAME="pybsadm"

APPSDIR="apps"
PROJDIR="project"
PRIVDIR=priv
ETCS=README.ru_ru.md requirements.txt start.sh manage.py .gitignore

FILES=$(APPSDIR) $(PROJDIR) $(PRIVDIR) $(ETCS) $(MAKEFILE_LIST)

REPO="repo"
DEB="$(REPO)/debsrc"

all: pack

clean_all: clean clean_repo clean_snapshots clean_pack

clean:
	#
	#	Удаляем скомпилированные файлы байт-кода питона.
	#
	@find ./ -name "*~" -type f -exec rm -f {} \;
	@find ./ -name "*.pyc" -type f -exec rm -f {} \;
	@find ./ -name "*.pyo" -type f -exec rm -f {} \;
	@find ./ -name __pycache__ -type d -exec rm -rf {} \;

install: 
	#
	#	Устанавливаем все зависимости, питоновского приложения.
	#
	@pip install -r requirements.txt

debuild: prepare_debuild
	#
	#	Собираем deb пакет.
	#
	@cd "$(DEB)" && @debuild

prepare_debuild: clean_deb
	#
	#	Подготавливаем директорию для сборки deb пакета.
	#
	@mkdir -p "$(DEB)/$(PROJNAME)"
	@cp -R "$(PRIVDIR)/support/debian" "$(DEB)/debian"
	@cp -R $(FILES) "$(DEB)/$(PROJNAME)"


clean_repo: clean_deb
	@rm -rf "$(REPO)"

clean_deb:
	@rm -rf "$(DEB)"


##
## Зададим имя архива с проектом.
##
PACKNAME=pybsadm

##
## Зададим расширение пакета с проектом.
##
PACKEXTN=tar.bz2

##
## Полное имя архива.
##
FULL_PACK_NAME=$(PACKNAME).$(PACKEXTN)


##
## Упакуем архив если его еще нет. 
## Псевдоним для цели `$(FULL_PACK_NAME)`.
##	
pack: | $(FULL_PACK_NAME)

##
## Упакуем архив если его еще нет.
##	
$(FULL_PACK_NAME):
	#
	#	Создаем архив из исходных кодов проекта и элементов Makefile.
	#
	@tar -cjf $@ $(FILES)

clean_pack:
	#
	# 	Удаляет архив.
	#
	@rm -f $(FULL_PACK_NAME);

##
## По `make repack` Перекуем архив, даже если он есть.
##
repack: clean_pack pack

##
## Полное имя для снимка проекта в текущий момент времени.
## C помощью -$(shell <Команда>) мы можем использовать команды bash.
##
SNAPSHOTPREFF=$(PACKNAME)-5nAp5h0t

SNAPSHOTNAME=$(SNAPSHOTPREFF)-$(shell date "+%Y-%m-%d_%H-%M-%S-%N").$(PACKEXTN)

snapshot:
	#
	# 	Создаем архив со снимком проекта.
	#
	@tar -cjf $(SNAPSHOTNAME) $(FILES)

clean_snapshots:
	#
	#	Удаляем все снимки проекта в папке.
	#
	@rm -f $(SNAPSHOTPREFF)*.$(PACKEXTN);
	
##
## Импровизированный вывод справки.
## Псевдоним для цели `help`.
##
man: help

##
## Импровизированный вывод справки.
## 
help:
	@less README.ru_ru.md

	
.PHONY: all clean install-python2 install-python3 help man
