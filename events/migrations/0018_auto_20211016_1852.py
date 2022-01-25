# Generated by Django 3.1.8 on 2021-10-16 17:52

import blog.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0017_auto_20210512_2232"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "h2",
                        blog.models.Heading2Block(form_classname="title", icon="title"),
                    ),
                    (
                        "h3",
                        blog.models.Heading3Block(form_classname="title", icon="title"),
                    ),
                    (
                        "h4",
                        blog.models.Heading4Block(form_classname="title", icon="title"),
                    ),
                    ("hr", blog.models.HRuleBlock()),
                    (
                        "paragraph",
                        wagtail.core.blocks.RichTextBlock(
                            features=[
                                "bold",
                                "italic",
                                "underline",
                                "h2",
                                "h3",
                                "h4",
                                "superscript",
                                "subscript",
                                "strikethrough",
                                "ol",
                                "ul",
                                "code",
                                "link",
                                "document-link",
                                "image",
                                "embed",
                            ],
                            icon="pilcrow",
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "pullquote",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("quote", wagtail.core.blocks.TextBlock("quote title")),
                                ("attribution", wagtail.core.blocks.CharBlock()),
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
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.core.blocks.ChoiceBlock(
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
                                ("code", wagtail.core.blocks.TextBlock(rows=15)),
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
                        "collapsible",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "visible_text",
                                    wagtail.core.blocks.TextBlock(label="Visible Text"),
                                ),
                                (
                                    "hidden_content",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "underline",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "superscript",
                                            "subscript",
                                            "strikethrough",
                                            "ol",
                                            "ul",
                                            "code",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                        ],
                                        label="Hidden Content",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("callout", blog.models.CalloutBlock()),
                    (
                        "html",
                        wagtail.core.blocks.StructBlock(
                            [("value", wagtail.core.blocks.TextBlock(rows=15))]
                        ),
                    ),
                    ("pdf", blog.models.PDFEmbedBlock()),
                ]
            ),
        ),
    ]
