Buat crontab untuk reminder:

# DOA PAGI
#10 08 * * MON,THU ajinha /usr/bin/python3 -c 'from workdir.python.botTelegram.bribot.multiFunction import doaPagi; doaPagi()'

# DAILY SYNC
#15 09 * * MON,THU ubuntu /usr/bin/python3 -c 'from workdir.python.botTelegram.bot.multiFunction import dailySync; dailySync()'
#40 08 * * TUE,WED,FRI ubuntu /usr/bin/python3 -c 'from workdir.python.botTelegram.bot.multiFunction import dailySync; dailySync()


sesuaikan crontab environment:
workdir.python.botTelegram.bot disesuaikan dengan file path script berada, misal: ~/workdir/python/botTelegram/bot
ubuntu, user disesuaikan dgn user yang akan melakukan eksekusi script.
