# windbg vmware windows内存导出

---

### 所需软件和工具

* 1.winDdg6.6.07.5

    > 任意版本均可，[我用的x86版][1]

* 2.VMWare10

* 3.windows 系统镜像文件


### 环境配置和安装过程

* 1.VMWare上面安装windows 虚拟机

* 2.安装windbg

    * 配置符号搜索路径：

        通过 File→Symbol File Path，输入

        SRV\*E:\windbg_path\windbgsymbols\*http://msdl.microsoft.com/download/symbols

* 3.配置windbg和windows虚拟机之间的com串口，搭建调试环境

    * 配置调试window XP的环境

        [Xp+WinDBG+VMware调试内核][5]

    备注：

    1.xp C:\boot.ini 文件最后添加一行，如下

    > multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="MicrosoftWindows XP Professional Debug" /fastdetect /debug /debugport=com1 /baudrate=115200

    其中'debugport=com1',根据VmWare添加串口的时候，名称为串行端口 2,则改为'debugport=com2',否则会导致连接不上

    * 配置调试window 7,8的环境

        [使用 vmware+windbg 分析调试 windows 7 内核][2]

* 4.配置pykd

    pykd在windbg里面加载后运行。因此，需要下载一个windbg支持Python语言的插件pykd.pyd，

    * [下载python][4]，我下载python2.7.8(windows x86)

    * [下载pykd.pyd][3]

        1. [下载正确的zip包][3](下载pykd-0.2.0.29-python-2.7.zip这个压缩包），接着提取并运行vcredist_x86.exe
        2. 下载exe程序(python2.7 x86版),接着执行它
        3. 开启cmd，切换到 C:\Program Files\Common Files\Microsoft Shared\VC下， 执行注册命令 regsvr32 msdia90.dll 系统会弹窗显示成功

    * 操作

        1.windbg成功连接上VMWare里面的windows系统
        2.在windbg命令行里面输入 .load pykd.pyd  (.load E:\path to\x86\pykd.pyd)
        3.接着输入 !py get_x86memory.py ,即可以运行程序

* 5.编写程序

    利用windbg调试工具导出windows虚拟机的内存信息。由于内存页面大小在win32系统中一般是4K，对于共4G大小的内存文件，我们在程序中从低地址将内存页面一页一页写进文本文件，这里是对于不同的系统，文件名分别是xp_whole_memory，win7_whole_memory和win8_whole_memory二进制文件。又因为内存中有很多地方没有信息，即所谓的缺页，为了方便以后的研究，我们有必要将这些没有的信息的页面的地址记录下来，存在mark_missing_address.txt文件里面。值得一提的是在导出内存是，我们将没有信息的页面全部用0填充。

    * 获取x86内存文件: get_x86memory.py

    备注
    * 1.get_x86memory.py

        > 程序中，需要手动设置要保存文件的路径

    * 2.导入pykd.pyd文件失败

        > 下载的插件版本和本地安装的python版本不一致
        > windbg死掉？(还不清楚原因)

* 6.需要十个小时的等待，就能得到内存文件了。


[1]: http://msdl.microsoft.com/download/symbols/debuggers/dbg_x86_6.6.07.5.exe
[2]: http://blog.chinaunix.net/uid-23254875-id-341011.html
[3]: http://pykd.codeplex.com/releases
[4]: https://www.python.org/downloads/
[5]: http://www.cnblogs.com/lzjsky/archive/2010/12/14/1905275.html

