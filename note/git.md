# git

### 基本命令

* rm

    + git rm --cached <file>

    直接从暂存区删除文件，工作区则不做出改变

* checkout

    + "git checkout ." 或 "git checkout -- <file>"

    会用暂存区全部或指定的文件替换工作区的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动

* fetch

    +git fetch origin master
    + git merge FETCH_HEAD

### 工作区与版本库
![Alt 图解](git-stage.png)
