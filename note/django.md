# django

---

## 参考

<a href="http://zozoz.github.io/myblog/2015/08/28/django%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%BD%91%E7%AB%99/" >Django快速建网站</a>

### 基本命令

* django-admin startproject project_name

* django-admin startapp app_name

* python manage.py makemigrations

* python manage.py migrate

* python manage.py runserver

* python manage.py collectstatic

> 需要先配置 STATIC_ROOT

* 国际化

根目录下面创建一个locale文件夹，然后使用命令创建国际化文件：

    + django-admin.py makemessages -l zh_CN

    执行完后，locale文件夹下面创建zh_CN/LC_MESSAGES/django.po
    写好了所有的翻译后执行：

    + django-admin.py compilemessages

    生成文件zh_CN/LC_MESSAGES/django.mo，最终的目标文件

### 模板

* 1.基本

> [S]: {% tag %}
> [D]: {% tag %} ... {% endtag %}

* entends[S]

> 告诉模板引擎，这个模板继承了另一个模板

* load[S]

> 读入一个自定义的模板库

* include[S]

> 允许在模板中包含其它的模板的内容

* block[D]

> 告诉模板引擎，子模板可以重载这些部分

* 2. 翻译

* trans[S] --To enable it, set USE_I18N to True, then load it with {% load i18n %}

> 标记需要翻译的字符串

不允许使用模板中的变量，只能使用单引号或双引号中的字符串

* blocktrans[S]

> 标记需要翻译的字符串

可以使用模板中的变量

* 3.安全

* csrf_token[S]

> 跨站请求伪造保护标签，在提交表单中需要添加

### 注释

> {# add some comment #}

### 备注

国际化 -- Internationalization，i 和 n 之间有 18 个字母，简称 I18N,。
本地化 -- localization， l 和 n 之间有 10 个字母，简称 L10N

### some examples

* 1.block.supper

\# Template: A.html
<html>
    <head></head>
    <body>
        {% block hello %}
            HELLO 
        {% endblock %}
    </body>
</html>

\# Template B.html
{% extends "A.html" %}
{% block hello %}
World
{% endblock %}

\# Rendered Template B
<html>
    <head></head>
    <body>
World
    </body>
</html>

\# Template C
{% extends "A.html" %}
{% block hello %}
{{ block.super }} World
{% endblock %}


\# Rendered Template C
<html>
    <head></head>
    <body>
Hello World
    </body>
</html>
