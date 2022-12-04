# Generated by Django 3.1 on 2020-08-14 15:58

import blog.models
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0017_auto_20200813_2311"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("h2", blog.models.Heading2Block(classname="title", icon="title")),
                    ("h3", blog.models.Heading3Block(classname="title", icon="title")),
                    ("h4", blog.models.Heading4Block(classname="title", icon="title")),
                    ("hr", blog.models.HRuleBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote", wagtail.blocks.TextBlock("quote title")),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse"
                        ),
                    ),
                    (
                        "code",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("c", "C"),
                                            ("cmake", "CMake"),
                                            ("cpp", "C++"),
                                            ("csharp", "C#"),
                                            ("css", "CSS"),
                                            ("go", "Go"),
                                            ("haskell", "Haskell"),
                                            ("haxe", "Haxe"),
                                            ("html", "HTML"),
                                            ("java", "Java"),
                                            ("js", "JavaScript"),
                                            ("json", "JSON"),
                                            ("kotlin", "Kotlin"),
                                            ("lua", "Lua"),
                                            ("make", "Makefile"),
                                            ("perl", "Perl"),
                                            ("perl6", "Perl 6"),
                                            ("php", "PHP"),
                                            ("python", "Python"),
                                            ("python3", "Python 3"),
                                            ("ruby", "Ruby"),
                                            ("sql", "SQL"),
                                            ("swift", "Swift"),
                                            ("xml", "XML"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "table",
                        blog.models.HtmlTableBlock(
                            table_options={
                                "autoColumnSize": False,
                                "colHeaders": False,
                                "contextMenu": [
                                    "row_above",
                                    "row_below",
                                    "---------",
                                    "col_left",
                                    "col_right",
                                    "---------",
                                    "remove_row",
                                    "remove_col",
                                    "---------",
                                    "undo",
                                    "redo",
                                ],
                                "editor": "text",
                                "height": 108,
                                "minSpareRows": 0,
                                "renderer": "html",
                                "rowHeaders": False,
                                "startCols": 3,
                                "startRows": 3,
                                "stretchH": "all",
                            }
                        ),
                    ),
                    (
                        "html",
                        wagtail.blocks.StructBlock(
                            [("value", wagtail.blocks.TextBlock(rows=15))]
                        ),
                    ),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("h2", blog.models.Heading2Block(classname="title", icon="title")),
                    ("h3", blog.models.Heading3Block(classname="title", icon="title")),
                    ("h4", blog.models.Heading4Block(classname="title", icon="title")),
                    ("hr", blog.models.HRuleBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote", wagtail.blocks.TextBlock("quote title")),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse"
                        ),
                    ),
                    (
                        "code",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("c", "C"),
                                            ("cmake", "CMake"),
                                            ("cpp", "C++"),
                                            ("csharp", "C#"),
                                            ("css", "CSS"),
                                            ("go", "Go"),
                                            ("haskell", "Haskell"),
                                            ("haxe", "Haxe"),
                                            ("html", "HTML"),
                                            ("java", "Java"),
                                            ("js", "JavaScript"),
                                            ("json", "JSON"),
                                            ("kotlin", "Kotlin"),
                                            ("lua", "Lua"),
                                            ("make", "Makefile"),
                                            ("perl", "Perl"),
                                            ("perl6", "Perl 6"),
                                            ("php", "PHP"),
                                            ("python", "Python"),
                                            ("python3", "Python 3"),
                                            ("ruby", "Ruby"),
                                            ("sql", "SQL"),
                                            ("swift", "Swift"),
                                            ("xml", "XML"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "table",
                        blog.models.HtmlTableBlock(
                            table_options={
                                "autoColumnSize": False,
                                "colHeaders": False,
                                "contextMenu": [
                                    "row_above",
                                    "row_below",
                                    "---------",
                                    "col_left",
                                    "col_right",
                                    "---------",
                                    "remove_row",
                                    "remove_col",
                                    "---------",
                                    "undo",
                                    "redo",
                                ],
                                "editor": "text",
                                "height": 108,
                                "minSpareRows": 0,
                                "renderer": "html",
                                "rowHeaders": False,
                                "startCols": 3,
                                "startRows": 3,
                                "stretchH": "all",
                            }
                        ),
                    ),
                    (
                        "html",
                        wagtail.blocks.StructBlock(
                            [("value", wagtail.blocks.TextBlock(rows=15))]
                        ),
                    ),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="description",
            field=wagtail.fields.StreamField(
                [
                    ("h2", blog.models.Heading2Block(classname="title", icon="title")),
                    ("h3", blog.models.Heading3Block(classname="title", icon="title")),
                    ("h4", blog.models.Heading4Block(classname="title", icon="title")),
                    ("hr", blog.models.HRuleBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote", wagtail.blocks.TextBlock("quote title")),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse"
                        ),
                    ),
                    (
                        "code",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("c", "C"),
                                            ("cmake", "CMake"),
                                            ("cpp", "C++"),
                                            ("csharp", "C#"),
                                            ("css", "CSS"),
                                            ("go", "Go"),
                                            ("haskell", "Haskell"),
                                            ("haxe", "Haxe"),
                                            ("html", "HTML"),
                                            ("java", "Java"),
                                            ("js", "JavaScript"),
                                            ("json", "JSON"),
                                            ("kotlin", "Kotlin"),
                                            ("lua", "Lua"),
                                            ("make", "Makefile"),
                                            ("perl", "Perl"),
                                            ("perl6", "Perl 6"),
                                            ("php", "PHP"),
                                            ("python", "Python"),
                                            ("python3", "Python 3"),
                                            ("ruby", "Ruby"),
                                            ("sql", "SQL"),
                                            ("swift", "Swift"),
                                            ("xml", "XML"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "table",
                        blog.models.HtmlTableBlock(
                            table_options={
                                "autoColumnSize": False,
                                "colHeaders": False,
                                "contextMenu": [
                                    "row_above",
                                    "row_below",
                                    "---------",
                                    "col_left",
                                    "col_right",
                                    "---------",
                                    "remove_row",
                                    "remove_col",
                                    "---------",
                                    "undo",
                                    "redo",
                                ],
                                "editor": "text",
                                "height": 108,
                                "minSpareRows": 0,
                                "renderer": "html",
                                "rowHeaders": False,
                                "startCols": 3,
                                "startRows": 3,
                                "stretchH": "all",
                            }
                        ),
                    ),
                    (
                        "html",
                        wagtail.blocks.StructBlock(
                            [("value", wagtail.blocks.TextBlock(rows=15))]
                        ),
                    ),
                ]
            ),
        ),
    ]
