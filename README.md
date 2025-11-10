## ZABBIX CONFIG

- настройки Zabbix server
- настройки Zabbix agent
    - скрипт ```statistics.py``` требует предварительной сборки с помощью консольного приложения    
    [PyInstaller](https://pyinstaller.org/en/stable/), так как в образе ```zabbix/zabbix-agent2:ubuntu-*.*.*```   
    отсутствует интерпретатор языка Python
- исходный код консольного приложения [```zbxtools```](https://github.com/techvsol/zbxtools) 