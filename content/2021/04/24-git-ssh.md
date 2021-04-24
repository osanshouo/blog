+++
title = "GitでSSH鍵を指定するとssh-agentと競合する"
date = 2021-04-24
[taxonomies]
tags = ["Linux"]
+++

Git 2.10 以降には [sshCommand](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand) というオプションがあり,
これを指定すればリポジトリ毎に ssh 鍵を指定して pull や push ができます.

* [git clone 時に秘密鍵を指定する](https://qiita.com/sonots/items/826b90b085f294f93acf)

ところが手元の環境ではうまくいかず, しばらく調べた結果, ssh-agent と競合しており, 
単に ssh 鍵を指定しただけでは ssh-agent に登録されている別の鍵が使用されているとわかりました.
その場合, ssh コマンドに `-o IdentitiesOnly=yes` というオプションを追加すれば解決します.

```bash
git config --local core.sshCommand 'ssh -i ~/.ssh/id_rsa -o IdentitiesOnly=yes -F /dev/null'
```

* [ssh - Disable SSHAgent with command line option - Stack Overflow](https://stackoverflow.com/questions/26258157/disable-sshagent-with-command-line-option)
