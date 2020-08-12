# Generated by Django 3.1 on 2020-08-12 12:54

import blog.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventtype_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', blog.models.Heading2Block(classname='title', icon='title')), ('h3', blog.models.Heading3Block(classname='title', icon='title')), ('h4', blog.models.Heading4Block(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('c', 'C'), ('cmake', 'CMake'), ('cpp', 'C++'), ('csharp', 'C#'), ('css', 'CSS'), ('go', 'Go'), ('haskell', 'Haskell'), ('haxe', 'Haxe'), ('html', 'HTML'), ('java', 'Java'), ('js', 'JavaScript'), ('json', 'JSON'), ('kotlin', 'Kotlin'), ('lua', 'Lua'), ('make', 'Makefile'), ('perl', 'Perl'), ('perl6', 'Perl 6'), ('php', 'PHP'), ('python', 'Python'), ('python3', 'Python 3'), ('ruby', 'Ruby'), ('sql', 'SQL'), ('swift', 'Swift'), ('xml', 'XML')])), ('code', wagtail.core.blocks.TextBlock())])), ('html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.TextBlock())]))]),
        ),
    ]
